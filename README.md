Prerequisites:
--------------

 - [**FFmpeg**](https://www.ffmpeg.org/)
 - [**Python**](https://www.python.org/)
 - Make sure both commands (`ffmpeg` and `python`) are accessible from the command line.

Instructions:
-------------

### Convert videos

Use `converter.py` to convert every supported video file in a folder to a target extension.

```bash
python converter.py <folder> <ext>
```

Examples:

```bash
python converter.py . wmv
python converter.py C:\Videos .mp4
```

Arguments:

 - `<folder>`: Folder containing the input video files.
 - `<ext>`: Target output extension. It can be passed with or without the leading dot, for example `wmv` or `.wmv`.

Behavior:

 - The script scans the provided folder and converts files with these extensions: `mp4`, `avi`, `wmv`, `mkv`, `mpg`.
 - Output files are written into the same folder.
 - If an output file name already exists, the script generates a numeric file name such as `00.wmv`, `01.wmv`, or `10.wmv` instead of overwriting the existing file.
 - Conversion uses FFmpeg with `-q:v 0`, which is the current fixed quality setting in the script.

If you want to invoke it through [converter.cmd](converter.cmd), make sure the repository folder is available in `PATH` and pass the same arguments:

```bash
converter <folder> <ext>
```

### Merge videos

Execute `merge` to place all the videos of the folder in one.

## Notes

 - To support additional input extensions, update `VIDEO_EXTENSIONS` in [converter.py](converter.py).
 - This project should be joined with the project [concat-videos](https://github.com/hrkns/concat-videos) at some point.