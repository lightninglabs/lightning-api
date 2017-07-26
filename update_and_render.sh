# Fetch the latest rpc.proto
curl -o rpc.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/lnrpc/rpc.proto

# Generate the rpc.json file from rpc.proto, so that generate_slate_docs.py can parse it
protoc -I. -I$GOPATH/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis --doc_out=json,rpc.json:. rpc.proto

# Generate the new docs
python render.py
