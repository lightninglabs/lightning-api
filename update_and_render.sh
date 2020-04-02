#!/bin/bash

set -e

LND_DIR="$GOPATH/src/github.com/lightningnetwork/lnd"
EXPERIMENTAL_PACKAGES="${EXPERIMENTAL_PACKAGES:-signrpc walletrpc chainrpc invoicesrpc watchtowerrpc}"
PROTO_DIR="${PROTO_DIR:-build/protos}"
WS_ENABLED="${WS_ENABLED:-true}"
GITHUB_URL="https://github.com/lightningnetwork/lnd"

rm -rf $PROTO_DIR

# We'll default to fetching the latest version of the RPC files. Otherwise, we'll use the commit hash provided.
commit="master"
[ -n "$1" ] && commit=$1

# Update lncli to the respective commit.
pushd $LND_DIR
COMMIT=$(git rev-parse HEAD)
if [ $commit != "nocompile" ]; then
  git reset --hard HEAD
  git pull
  git checkout $commit
  COMMIT=$(git rev-parse HEAD)
  make clean && make && make install tags="$EXPERIMENTAL_PACKAGES"
fi
popd

# Copy over all proto and json files from the checked out lnd source directory.
mkdir -p $PROTO_DIR
rsync -a --prune-empty-dirs --include '*/' --include '*.proto' --include '*.json' --exclude '*' $LND_DIR/lnrpc/ $PROTO_DIR/

pushd $PROTO_DIR
protoc -I. -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
  --doc_out=json,generated.json:. *.proto **/*.proto
popd

# Render the new docs.
export EXPERIMENTAL_PACKAGES PROTO_DIR WS_ENABLED COMMIT GITHUB_URL
./render.py

# Clean up.
rm -rf $PROTO_DIR
