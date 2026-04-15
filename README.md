# jrc-grids

Tiled grids of open JRC data for use with [gridviz](https://github.com/eurostat/gridviz)

## Steps:

1 update config.py with your values
2 run `python pipeline.py air-filtration_map_use_tonnes_2021` for a single file (TIF)

You can run the pipeline for all TIF files in a folder like so:

#### Safer

python batch_pipeline.py --workers 2 --tile-workers 2 --overwrite

#### More aggressive

python batch_pipeline.py --workers 3 --tile-workers 3 --no-overwrite

## Examples

- European forests: see [tiled-europe-forest](https://github.com/jgaffuri/tiled-europe-forest)
