from concurrent.futures import ProcessPoolExecutor, as_completed
import argparse
import time
import pipeline
from config import INPUT_DIR


def format_time(seconds):
    m, s = divmod(seconds, 60)
    return f"{int(m)}m {s:.1f}s"


def run_one(base_name: str, overwrite: bool, tile_workers: int):
    pipeline.run(
        base_name=base_name,
        overwrite=overwrite,
        tile_workers=tile_workers
    )


def run_batch(overwrite=True, max_workers=3, tile_workers=5, limit=None):
    start = time.perf_counter()

    tif_files = sorted(
        tif for tif in INPUT_DIR.glob("*.tif")
        if "_filtered" not in tif.stem
    )

    if limit is not None:
        tif_files = tif_files[:limit]

    base_names = [tif.stem for tif in tif_files]

    print(f"Found {len(base_names)} TIFFs")
    print(f"Dataset workers: {max_workers}")
    print(f"Tile workers per dataset: {tile_workers}")
    print(f"Overwrite: {overwrite}")

    success = 0
    failed = 0

    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(run_one, base_name, overwrite, tile_workers): base_name
            for base_name in base_names
        }

        for future in as_completed(futures):
            base_name = futures[future]
            try:
                future.result()
                print(f"OK: {base_name}")
                success += 1
            except Exception as e:
                print(f"FAILED: {base_name}")
                print(e)
                failed += 1

    total = time.perf_counter() - start
    print(f"\nSuccess: {success}")
    print(f"Failed: {failed}")
    print(f"Batch done in {format_time(total)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch process TIFFs through the raster pipeline.")
    parser.add_argument(
        "--workers",
        type=int,
        default=3,
        help="Number of datasets to process in parallel."
    )
    parser.add_argument(
        "--tile-workers",
        type=int,
        default=5,
        help="Number of processors to use inside tiling for each dataset."
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=None,
        help="Only process the first N TIFFs."
    )

    overwrite_group = parser.add_mutually_exclusive_group()
    overwrite_group.add_argument(
        "--overwrite",
        dest="overwrite",
        action="store_true",
        help="Overwrite existing outputs."
    )
    overwrite_group.add_argument(
        "--no-overwrite",
        dest="overwrite",
        action="store_false",
        help="Skip existing outputs."
    )
    parser.set_defaults(overwrite=True)

    args = parser.parse_args()

    run_batch(
        overwrite=args.overwrite,
        max_workers=args.workers,
        tile_workers=args.tile_workers,
        limit=args.limit
    )