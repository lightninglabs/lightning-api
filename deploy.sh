#!/bin/sh
bundle exec middleman build --clean

# -m use faster multithreaded uploads
# -d delete remote files that aren't in the source
# -r recurse into source subdirectories
gsutil -m rsync -d -r ./build gs://api.lightning.community
