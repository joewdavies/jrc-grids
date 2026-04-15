from pathlib import Path

BASE_DIR = Path("../tmp")

INPUT_DIR = BASE_DIR / "input"
PROCESSED_DIR = BASE_DIR / "processed"
OUTPUT_DIR = BASE_DIR / "output"

RESOLUTIONS = [50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]
NODATA_VALUE  = -9999.0

GDALWARP = Path(r"C:\Users\jwd10\AppData\Local\Programs\OSGeo4W\bin\gdalwarp.exe")


# ---- RAW ----
def raw_file(base_name: str) -> Path:
    return INPUT_DIR / f"{base_name}.tif"


# ---- FILTERED ----
def filtered_file(base_name: str) -> Path:
    return PROCESSED_DIR / base_name / "filtered.tif"


# ---- AGGREGATED ----
def aggregated_dir(base_name: str) -> Path:
    return PROCESSED_DIR / base_name / "aggregated"

def aggregated_file(base_name: str, res: int) -> Path:
    return aggregated_dir(base_name) / f"{base_name}_{res}.tif"


# ---- TILES ----
def tiles_dir(base_name: str, res: int) -> Path:
    return OUTPUT_DIR / base_name / str(res)