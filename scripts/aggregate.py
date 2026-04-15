import subprocess

from config import RESOLUTIONS, GDALWARP, filtered_file, aggregated_file, aggregated_dir

def run(base_name: str, overwrite=True):
    print(f"=== AGGREGATE {base_name} ===")

    aggregated_dir(base_name).mkdir(parents=True, exist_ok=True)

    for res in RESOLUTIONS:
        output = aggregated_file(base_name, res)

        if output.exists() and not overwrite:
            print(f"{res} exists, skipping")
            continue

        print(res)

        cmd = [
            str(GDALWARP),
            "-tr", str(res), str(res),
            "-r", "average",
            "-tap",
            str(filtered_file(base_name)),
            str(output)
        ]

        if overwrite:
            cmd.insert(1, "-overwrite")

        subprocess.run(cmd, check=True)

if __name__ == "__main__":
    run("air-filtration_map_use_tonnes_2021", overwrite=True)