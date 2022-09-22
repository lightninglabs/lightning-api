#!/bin/bash

set -e -x

rm -rf build/loop build/lnd build/faraday build/pool build/taro
cp -r build/all build/loop
cp -r build/all build/faraday
cp -r build/all build/pool
cp -r build/all build/taro
mv build/all build/lnd
cp build/loop/loop.html build/loop/index.html
cp build/lnd/lnd.html build/lnd/index.html
cp build/faraday/faraday.html build/faraday/index.html
cp build/pool/pool.html build/pool/index.html
cp build/taro/taro.html build/taro/index.html
