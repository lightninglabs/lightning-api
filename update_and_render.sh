# We'll default to fetching the latest version of the RPC files. Otherwise, we'll use the commit hash provided.
commit="master"
[ -n "$1" ] && commit=$1

curl -o rpc.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/$commit/lnrpc/rpc.proto
curl -o rpc.swagger.json -s https://raw.githubusercontent.com/lightningnetwork/lnd/$commit/lnrpc/rpc.swagger.json

# Generate the rpc.json file from rpc.proto, so that render.py can parse it.
protoc -I. -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis --doc_out=json,rpc.json:. rpc.proto

# Update lncli to the respective commit.
pushd $GOPATH/src/github.com/lightningnetwork/lnd
git reset --hard HEAD
git pull
git checkout $commit
make
make install
popd

# Render the new docs.
./render.py

# Clean up.
rm rpc.proto rpc.json rpc.swagger.json
