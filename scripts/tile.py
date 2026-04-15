from pygridmap import gridtiler_raster
import shutil

from config import RESOLUTIONS, NODATA_VALUE, aggregated_file, tiles_dir

def run(base_name: str, overwrite=True, num_processors_to_use=3):
    print(f"=== TILE {base_name} ===")

    for res in RESOLUTIONS:
        out_dir = tiles_dir(base_name, res)

        if out_dir.exists():
            if overwrite:
                print(f"{res} exists, overwriting")
                shutil.rmtree(out_dir)
            else:
                print(f"{res} exists, skipping")
                continue
        else:
            print(res)

        gridtiler_raster.tiling_raster(
            {
                base_name: {
                    "file": str(aggregated_file(base_name, res)),
                    "band": 1,
                    "no_data_values": [NODATA_VALUE]
                },
            },
            str(out_dir),
            tile_size_cell=256,
            format="parquet",
            num_processors_to_use=num_processors_to_use
        )

if __name__ == "__main__":
    run("example_name", overwrite=True, num_processors_to_use=3)