#!/bin/bash

docker pull guggero/lightning-api

docker rm -f flask-api-server 2>/dev/null || echo "Container not running yet, starting new one"

docker run \
  -d \
  -p 5000:5000 \
  -e WEBHOOK_SECRET_TOKEN \
  -v $HOME/.config:/root/.config \
  -v $PWD/build:/tmp/work/build \
  -v $PWD/templates:/tmp/work/templates \
  -v $PWD/source:/tmp/work/source \
  --name flask-api-server \
  --restart unless-stopped \
  guggero/lightning-api \
  python3 -m flask run --host=0.0.0.0
