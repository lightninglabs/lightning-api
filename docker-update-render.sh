#!/bin/bash

set -e -x

docker build -t local/lightning-api .

docker run \
  --rm \
  -v $PWD/source:/tmp/work/source \
  local/lightning-api \
  ./update.sh
