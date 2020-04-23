#!/bin/bash

docker rm -f flask-api-server 2>&1 || echo "Container not running yet, starting new one"

docker run \
  -d \
  -p 5000:5000 \
  -e WEBHOOK_SECRET_TOKEN \
  --name flask-api-server \
  --restart unless-stopped \
  local/lightning-api \
  python3 -m flask run --host=0.0.0.0
