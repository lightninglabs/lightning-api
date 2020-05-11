#!/bin/sh
bundle exec middleman build --clean

# Separate the individual projects so they can be deployed to different locations.
rm -rf build/loop build/lnd
cp -r build/all build/loop
mv build/all build/lnd
cp build/loop/loop.html build/loop/index.html
cp build/lnd/lnd.html build/lnd/index.html


# -m use faster multithreaded uploads
# -d delete remote files that aren't in the source
# -r recurse into source subdirectories
gsutil -m rsync -d -r ./build/lnd gs://api.lightning.community
gsutil -m rsync -d -r ./build/loop gs://loop.lightning.today/docs
