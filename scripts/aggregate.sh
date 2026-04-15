#!/bin/bash

INPUT_FILE="../tmp/input/air-filtration_map_use_tonnes_2021_filtered.tif"
OUTPUT_FOLDER="../tmp/input"
RESOLUTIONS=(50000 20000 10000 5000 2000 1000 500 200 100)
RESAMPLE_METHOD="average"
GDALWARP="/c/Users/jwd10/AppData/Local/Programs/OSGeo4W/bin/gdalwarp"

BASENAME=$(basename "$INPUT_FILE" .tif)

for res in "${RESOLUTIONS[@]}"; do
    echo "$res"
    $GDALWARP -tr $res $res -r $RESAMPLE_METHOD -tap \
        "$INPUT_FILE" \
        "$OUTPUT_FOLDER/${BASENAME}_${res}.tif"
done