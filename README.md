# jrc-grids

Tiled grids of open JRC data for use with [gridviz](https://github.com/eurostat/gridviz)

## Steps:

1 `python filter.py` // remove 'no data' etc  
2 `bash aggregate.sh` // create multipe resolutions (e.g. 10k, 5km etc)  
3 `python tile.py` // create tiles for gridviz

## Examples

- European forests: see [tiled-europe-forest](https://github.com/jgaffuri/tiled-europe-forest)
