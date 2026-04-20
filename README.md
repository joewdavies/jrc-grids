# jrc-grids

Tiled grids of open JRC data for use with [gridviz](https://github.com/eurostat/gridviz)

## Steps:

1 update config.py with your values  
2 run `python pipeline.py nameOfTifFile --tile-workers 6` for a single file (TIF)

You can run the pipeline for all TIF files in a folder like so:

`python batch_pipeline.py --workers 2 --tile-workers 2 --overwrite`

where:

`--workers` = Number of datasets to process in parallel.

and

`--tile-workers` = Number of processors to use inside tiling for each dataset.

## Examples

- INCA: [demo](https://joewdavies.github.io/jrc-grids/example/)
- European forests: see [tiled-europe-forest](https://github.com/jgaffuri/tiled-europe-forest)

- For the following datasets: [check out this demo](https://github.com/joewdavies/jrc-grids/example)
  - air-filtration_map_use_tonnes_2021
  - carbon-net-sequestration_map_use_monetary_EURO-real_2021
  - carbon-net-sequestration_map_use_tonnes_2021
  - carbon-retention_map_closing-stock_tonnes_2021
  - crop-pollination_map_demand_hectares_2021
  - crop-pollination_map_supply_EURO-current_2021
  - crop-pollination_map_supply_EURO-real_2021
  - crop-pollination_map_supply_tonnes_2021
  - crop-pollination_map_unmet_hectares_2021
  - crop-pollination_map_use_EURO-current_2021
  - crop-pollination_map_use_EURO-real_2021
  - crop-pollination_map_use_tonnes_2021
  - crop-pollination-long_map_potential_SPA_binary_2021
  - crop-pollination-short_map_potential_SPA_binary_2021
  - crop-provision_map_use_EURO-real_2021
  - crop-provision_map_use_tonne_2021
  - flood-control_map_mismatch_hectare_2018
  - flood-control_map_unmet_demand_population_2018
  - flood-control_map_use_hectare_2018
  - flood-control_map_use_population_2018
  - flood-control_map_value_EURO-real_2018
  - Soil-Retention_map_mismatch_tonnes_2021
  - Soil-Retention_map_potential_ratio_2021
  - Soil-Retention_map_use_tonnes_2021
  - Soil-Retention_map_use-cropland_EURO-real_2021

## Commands

python pipeline.py flood-control_map_use_population_2018 --tile-workers 11
