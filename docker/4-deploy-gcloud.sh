#!/bin/bash

set -e -x

docker pull guggero/lightning-api

# gsutil flags:
# -m use faster multithreaded uploads
# -d delete remote files that aren't in the source
# -r recurse into source subdirectories

docker run \
  --rm \
  -v $HOME/.config:/root/.config \
  -v $PWD/build:/tmp/work/build \
  guggero/lightning-api \
  gsutil -m rsync -d -r ./build/lnd gs://api.lightning.community

docker run \
  --rm \
  -v $HOME/.config:/root/.config \
  -v $PWD/build:/tmp/work/build \
  guggero/lightning-api \
  gsutil -m rsync -d -r ./build/loop gs://lightning.engineering/loopapi
