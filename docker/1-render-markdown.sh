#!/bin/bash

set -e -x

docker pull guggero/lightning-api

docker run \
  --rm \
  -e WS_ENABLED \
  -e LND_FORK \
  -e LND_COMMIT \
  -e LOOP_FORK \
  -e LOOP_COMMIT \
  -e FARADAY_FORK \
  -e FARADAY_COMMIT \
  -e POOL_FORK \
  -e POOL_COMMIT \
  -v $PWD/build:/tmp/work/build \
  -v $PWD/templates:/tmp/work/templates \
  -v $PWD/source:/tmp/work/source \
  guggero/lightning-api \
  ./update.sh
