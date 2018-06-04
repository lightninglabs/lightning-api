# Fetch the latest rpc.proto
curl -o rpc.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/lnrpc/rpc.proto
# cp ~/lightning/ln-lnd/src/github.com/lightningnetwork/lnd/lnrpc/rpc.proto .

# Generate the rpc.json file from rpc.proto, so that generate_slate_docs.py can parse it
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

# Clean up
rm rpc.proto
rm rpc.json
