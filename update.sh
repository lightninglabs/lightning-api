#!/bin/bash

set -e

function compile() {
  PROTO_DIR=$PROTO_ROOT_DIR/$COMPONENT
  LOCAL_REPO_PATH=/tmp/apidoc/$COMPONENT
  if [[ ! -d $LOCAL_REPO_PATH ]]; then
    git clone $REPO_URL $LOCAL_REPO_PATH
  fi

  # Update lncli to the respective commit.
  pushd $LOCAL_REPO_PATH
  COMMIT=$(git rev-parse HEAD)
  if [ $commit != "nocompile" ]; then
    git reset --hard HEAD
    git pull
    git checkout $commit
    COMMIT=$(git rev-parse HEAD)
    eval $INSTALL_CMD
  fi
  popd

  # Copy over all proto and json files from the checked out lnd source directory.
  mkdir -p $PROTO_DIR
  rsync -a --prune-empty-dirs --include '*/' --include '*.proto' --include '*.json' --exclude '*' $LOCAL_REPO_PATH/$PROTO_SRC_DIR/ $PROTO_DIR/

  pushd $PROTO_DIR
  proto_files=$(find . -name '*.proto' -not -name $EXCLUDE_PROTOS)
  protoc -I. -I/usr/local/include \
    -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
    --doc_out=json,generated.json:. $proto_files
  popd

  # Render the new docs.
  cp templates/${COMPONENT}_header.md $APPEND_TO_FILE
  export EXPERIMENTAL_PACKAGES PROTO_DIR PROTO_SRC_DIR WS_ENABLED COMMIT REPO_URL COMMAND COMPONENT APPEND_TO_FILE
  ./render.py
  cat templates/${COMPONENT}_footer.md >> $APPEND_TO_FILE
}

# Generic options.
WS_ENABLED="${WS_ENABLED:-false}"
PROTO_ROOT_DIR="build/protos"

# Remove previously generated templates.
rm -rf $PROTO_ROOT_DIR
rm -rf source/*.html.md

# We'll default to fetching the latest version of the RPC files. Otherwise, we'll use the commit hash provided.
commit="master"
[ -n "$1" ] && commit=$1

########################
## Compile docs for lnd
########################
REPO_URL="https://github.com/lightningnetwork/lnd"
COMPONENT=lnd
COMMAND=lncli
PROTO_SRC_DIR=lnrpc
EXCLUDE_PROTOS="none"
EXPERIMENTAL_PACKAGES="signrpc walletrpc chainrpc invoicesrpc watchtowerrpc"
INSTALL_CMD="make clean && make install tags=\"$EXPERIMENTAL_PACKAGES\""
APPEND_TO_FILE=source/lnd.html.md
compile

########################
## Compile docs for loop
########################
REPO_URL="https://github.com/lightninglabs/loop"
COMPONENT=loop
COMMAND=loop
PROTO_SRC_DIR=looprpc
EXCLUDE_PROTOS="server.proto"
EXPERIMENTAL_PACKAGES=""
INSTALL_CMD="go install ./..."
APPEND_TO_FILE=source/loop.html.md
compile

# Clean up.
rm -rf $PROTO_ROOT_DIR
