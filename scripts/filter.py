import rasterio
import numpy as np
from scipy.ndimage import binary_dilation

INPUT_FILE = "../tmp/input/air-filtration_map_use_tonnes_2021.tif"
OUTPUT_FILE = "../tmp/input/air-filtration_map_use_tonnes_2021_filtered.tif"

def expand_255(data):
    mask = data == 255
    structuring_element = np.array([[0, 1, 0],
                                    [1, 1, 1],
                                    [0, 1, 0]])
    expanded_mask = binary_dilation(mask, structure=structuring_element)
    data[expanded_mask] = 255
    return data

def process(input_file, output_file):
    with rasterio.open(input_file) as src:
        data = src.read(1)
        data[data > 100] = 255
        data = expand_255(data)
        data[data > 100] = 0
        profile = src.profile
        profile.update(dtype=rasterio.uint8, nodata=0)
        with rasterio.open(output_file, 'w', **profile) as dst:
            dst.write(data, 1)

print("start")
process(INPUT_FILE, OUTPUT_FILE)
print("done")