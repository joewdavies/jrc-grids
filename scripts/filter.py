import rasterio
import numpy as np
from scipy.ndimage import binary_dilation

from config import NODATA_VALUE, raw_file, filtered_file


def expand_mask(mask: np.ndarray) -> np.ndarray:
    structuring_element = np.array([
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ], dtype=bool)
    return binary_dilation(mask, structure=structuring_element)


def process(input_file: str, output_file: str) -> None:
    with rasterio.open(input_file) as src:
        data = src.read(1).astype(np.float32)

        # Normalize NaN nodata to an explicit numeric nodata value
        data[np.isnan(data)] = NODATA_VALUE

        remove_mask = data > 100
        remove_mask = expand_mask(remove_mask)

        data[remove_mask] = NODATA_VALUE

        profile = src.profile.copy()
        profile.update(dtype=rasterio.float32, nodata=NODATA_VALUE)

        with rasterio.open(output_file, "w", **profile) as dst:
            dst.write(data, 1)


def run(base_name: str, overwrite=True):
    print(f"=== FILTER {base_name} ===")

    output = filtered_file(base_name)
    output.parent.mkdir(parents=True, exist_ok=True)

    if output.exists() and not overwrite:
        print("filtered file exists, skipping")
        return

    process(str(raw_file(base_name)), str(output))


if __name__ == "__main__":
    run("air-filtration_map_use_tonnes_2021", overwrite=True)