from pygridmap import gridtiler_raster

INPUT_FOLDER_PATH = "../tmp/input/"
OUTPUT_FOLDER_PATH = "../tmp/output/"

if __name__ == '__main__':
    print("start")
    for res in [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]:
        print(res)

        gridtiler_raster.tiling_raster(
            {
                "air-filtration_map_use_tonnes_2021": {
                    "file": INPUT_FOLDER_PATH + f"air-filtration_map_use_tonnes_2021_{res}.tif",
                    "band": 1,
                    "no_data_values": [255, 254, 0]
                },
            },
            OUTPUT_FOLDER_PATH + str(res),
            tile_size_cell=256,
            format="parquet",
            num_processors_to_use=6
        )