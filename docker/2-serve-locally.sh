#!/bin/bash

set -e -x

docker pull guggero/lightning-api

docker run \
  --rm \
  -p 4567:4567 \
  -v $PWD/source:/tmp/work/source \
  guggero/lightning-api \
  bundle exec middleman server
