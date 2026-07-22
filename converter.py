import argparse
from pathlib import Path
from subprocess import call

VIDEO_EXTENSIONS = {".mp4", ".avi", ".wmv", ".mkv", ".mpg"}


def has_valid_input_ext(file_path: Path) -> bool:
    return file_path.suffix.lower() in VIDEO_EXTENSIONS


def normalize_ext(ext: str) -> str:
    return ext if ext.startswith(".") else f".{ext}"


def main():
    parser = argparse.ArgumentParser(
        description="Convert video files in a folder to another extension using ffmpeg."
    )
    parser.add_argument(
        "path",
        help="Folder containing the input video files"
    )
    parser.add_argument(
        "ext",
        help="Target output extension, for example: .wmv or wmv"
    )

    args = parser.parse_args()

    path = Path(args.path).resolve()
    ext = normalize_ext(args.ext).lower()
    factor = "0"

    if not path.exists() or not path.is_dir():
        raise SystemExit(f"Error: '{path}' is not a valid folder.")

    onlyfiles = sorted(
        [f for f in path.iterdir() if f.is_file() and has_valid_input_ext(f)]
    )

    counter = 0

    for file in onlyfiles:
        print("*" * 66)
        print("*" * 66)
        print("*" * 66)
        print("*" * 66)
        print("*" * 66)
        print(f"### FILE #{counter}")

        newname = file.stem + ext
        target_path = path / newname

        if not target_path.is_file():
            call(["ffmpeg", "-i", str(file), "-q:v", factor, str(target_path)])
        else:
            append = "0" if counter < 10 else ""

            while (path / f"{append}{counter}{ext}").is_file():
                counter += 1
                if counter >= 10:
                    append = ""

            target_path = path / f"{append}{counter}{ext}"
            call(["ffmpeg", "-i", str(file), "-q:v", factor, str(target_path)])

        counter += 1


if __name__ == "__main__":
    main()
