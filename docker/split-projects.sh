#!/bin/bash

set -e -x

rm -rf build/loop build/lnd
cp -r build/all build/loop
mv build/all build/lnd
cp build/loop/loop.html build/loop/index.html
cp build/lnd/lnd.html build/lnd/index.html
