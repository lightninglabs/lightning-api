#!/bin/bash

set -e

function compile() {
  echo "Using ${COMPONENT} repo URL ${REPO_URL} and commit ${CHECKOUT_COMMIT}"

  PROTO_DIR=$PROTO_ROOT_DIR/$COMPONENT
  LOCAL_REPO_PATH=/tmp/$COMPONENT
  if [[ ! -d $LOCAL_REPO_PATH ]]; then
    git clone $REPO_URL $LOCAL_REPO_PATH
  fi

  # Update the repository to the respective CHECKOUT_COMMIT and install the binary.
  pushd $LOCAL_REPO_PATH
  COMMIT=$(git rev-parse HEAD)
  git reset --hard HEAD
  git pull
  git checkout $CHECKOUT_COMMIT
  COMMIT=$(git rev-parse HEAD)
  eval $INSTALL_CMD
  popd

  # Copy over all proto and json files from the checked out lnd source directory.
  mkdir -p $PROTO_DIR
  rsync -a --prune-empty-dirs --include '*/' --include '*.proto' --include '*.json' --exclude '*' $LOCAL_REPO_PATH/$PROTO_SRC_DIR/ $PROTO_DIR/

  pushd $PROTO_DIR
  proto_files=$(find . -name '*.proto' -not -name $EXCLUDE_PROTOS)
  protoc -I. -I/usr/local/include \
    --doc_out=json,generated.json:. $proto_files
  popd

  # Render the new docs.
  cp templates/${COMPONENT}_header.md $APPEND_TO_FILE
  export EXPERIMENTAL_PACKAGES PROTO_DIR PROTO_SRC_DIR WS_ENABLED COMMIT REPO_URL COMMAND COMPONENT APPEND_TO_FILE GRPC_PORT REST_PORT EXCLUDE_SERVICES
  ./render.py
  cat templates/${COMPONENT}_footer.md >> $APPEND_TO_FILE
}

# Generic options.
WS_ENABLED="${WS_ENABLED:-true}"
LND_FORK="${LND_FORK:-lightningnetwork}"
LND_COMMIT="${LND_COMMIT:-master}"
LOOP_FORK="${LOOP_FORK:-lightninglabs}"
LOOP_COMMIT="${LOOP_COMMIT:-master}"
FARADAY_FORK="${FARADAY_FORK:-lightninglabs}"
FARADAY_COMMIT="${FARADAY_COMMIT:-master}"
POOL_FORK="${POOL_FORK:-lightninglabs}"
POOL_COMMIT="${POOL_COMMIT:-master}"
PROTO_ROOT_DIR="build/protos"
TARO_FORK="${TARO_FORK:-lightninglabs}"
TARO_COMMIT="${TARO_COMMIT:-main}"

# Remove previously generated templates.
rm -rf $PROTO_ROOT_DIR
rm -rf source/*.html.md

########################
## Compile docs for lnd
########################
REPO_URL="https://github.com/${LND_FORK}/lnd"
CHECKOUT_COMMIT=$LND_COMMIT
COMPONENT=lnd
COMMAND=lncli
PROTO_SRC_DIR=lnrpc
EXCLUDE_PROTOS="none"
EXPERIMENTAL_PACKAGES="signrpc walletrpc chainrpc invoicesrpc watchtowerrpc"
INSTALL_CMD="make clean && make install tags=\"$EXPERIMENTAL_PACKAGES\""
APPEND_TO_FILE=source/lnd.html.md
GRPC_PORT=10009
REST_PORT=8080
compile

########################
## Compile docs for loop
########################
REPO_URL="https://github.com/${LOOP_FORK}/loop"
CHECKOUT_COMMIT=$LOOP_COMMIT
COMPONENT=loop
COMMAND=loop
PROTO_SRC_DIR=""
EXCLUDE_PROTOS="server.proto -not -name common.proto"
EXPERIMENTAL_PACKAGES=""
INSTALL_CMD="make install"
APPEND_TO_FILE=source/loop.html.md
GRPC_PORT=11010
REST_PORT=8081
compile

########################
## Compile docs for faraday
########################
REPO_URL="https://github.com/${FARADAY_FORK}/faraday"
CHECKOUT_COMMIT=$FARADAY_COMMIT
COMPONENT=faraday
COMMAND=frcli
PROTO_SRC_DIR=frdrpc
EXCLUDE_PROTOS="none"
EXPERIMENTAL_PACKAGES=""
INSTALL_CMD="make install"
APPEND_TO_FILE=source/faraday.html.md
GRPC_PORT=8465
REST_PORT=8082
compile

########################
## Compile docs for pool
########################
REPO_URL="https://github.com/${POOL_FORK}/pool"
CHECKOUT_COMMIT=$POOL_COMMIT
COMPONENT=pool
COMMAND=pool
PROTO_SRC_DIR=""
EXCLUDE_PROTOS="none"
EXCLUDE_SERVICES="ChannelAuctioneer"
EXPERIMENTAL_PACKAGES=""
INSTALL_CMD="make install"
APPEND_TO_FILE=source/pool.html.md
GRPC_PORT=12010
REST_PORT=8281
compile

########################
## Compile docs for taro
########################
REPO_URL="https://github.com/${TARO_FORK}/taro"
CHECKOUT_COMMIT=$TARO_COMMIT
COMPONENT=taro
COMMAND=tarocli
PROTO_SRC_DIR=""
EXCLUDE_PROTOS="none"
EXPERIMENTAL_PACKAGES=""
INSTALL_CMD="make install"
APPEND_TO_FILE=source/taro.html.md
GRPC_PORT=10029
REST_PORT=8089
compile
