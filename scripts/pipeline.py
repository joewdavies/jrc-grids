import argparse
import time
import filter
import aggregate
import tile

def format_time(seconds):
    m, s = divmod(seconds, 60)
    return f"{int(m)}m {s:.1f}s"

def timed_step(name, func, **kwargs):
    print(f"\n--- {name} START ---")
    start = time.perf_counter()
    func(**kwargs)
    elapsed = time.perf_counter() - start
    print(f"--- {name} DONE in {format_time(elapsed)} ---")

def run(base_name: str, overwrite=True, tile_workers=10):
    total_start = time.perf_counter()

    print(f"\n########## PROCESSING {base_name} ##########")

    timed_step("FILTER", filter.run, base_name=base_name, overwrite=overwrite)
    timed_step("AGGREGATE", aggregate.run, base_name=base_name, overwrite=overwrite)
    timed_step(
        "TILE",
        tile.run,
        base_name=base_name,
        overwrite=overwrite,
        num_processors_to_use=tile_workers
    )

    total = time.perf_counter() - total_start
    print(f"\n=== {base_name} DONE in {format_time(total)} ===")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run pipeline for a single TIFF")
    parser.add_argument("base_name", help="Filename without .tif")
    parser.add_argument("--tile-workers", type=int, default=10)

    overwrite_group = parser.add_mutually_exclusive_group()
    overwrite_group.add_argument("--overwrite", action="store_true")
    overwrite_group.add_argument("--no-overwrite", dest="overwrite", action="store_false")
    parser.set_defaults(overwrite=True)

    args = parser.parse_args()

    run(
        base_name=args.base_name,
        overwrite=args.overwrite,
        tile_workers=args.tile_workers
    )