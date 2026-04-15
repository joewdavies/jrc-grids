import rasterio
import numpy as np
from scipy.ndimage import binary_dilation

INPUT_FILE = "../tmp/input/air-filtration_map_use_tonnes_2021.tif"
OUTPUT_FILE = "../tmp/input/air-filtration_map_use_tonnes_2021_filtered.tif"

NODATA_VALUE = -9999.0

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

        remove_mask = data > 100
        remove_mask = expand_mask(remove_mask)

        data[remove_mask] = NODATA_VALUE

        profile = src.profile.copy()
        profile.update(dtype=rasterio.float32, nodata=NODATA_VALUE)

        with rasterio.open(output_file, "w", **profile) as dst:
            dst.write(data, 1)

print("start")
process(INPUT_FILE, OUTPUT_FILE)
print("done")