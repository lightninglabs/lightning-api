#!/bin/bash

set -e -x

docker build \
  -t guggero/lightning-api \
  docker/

docker push guggero/lightning-api
