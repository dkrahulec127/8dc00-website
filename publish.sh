#!/bin/bash

OUT_DIR="./docs/source/reader/public"

rm -rf $OUT_DIR
mkdir $OUT_DIR

cp -r * $OUT_DIR

# remove all lines between the lines #!studentstart and #!studentend
find $OUT_DIR -type f -name '2.5_CNNs_fundamental_building_blocks.ipynb' -exec sed -i '' -e '/#!studentstart/,/#!studentend/d;' {} \;