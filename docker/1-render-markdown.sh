#!/bin/bash

set -e -x

docker pull guggero/lightning-api

docker run \
  --rm \
  -v $PWD/build:/tmp/work/build \
  -v $PWD/templates:/tmp/work/templates \
  -v $PWD/source:/tmp/work/source \
  guggero/lightning-api \
  ./update.sh
