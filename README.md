Prerrequisites:
---------------

 - [**FFmpeg**](https://www.ffmpeg.org/)
 - [**Python**](https://www.python.org/)
 - Make sure both commands (`ffmpef` and `python` are accesible through the command line).

Instructions:
-------------

 - Make sure the `PATH` variable contains the repository folder route.
 - Open the console and place it in the folder where the videos are in.
 - Execute the command `converter` to convert a set of videos of the folder to another format.
 - Execute the command `merge` to place all the videos of the folder in one.

## Notes:##

 - It only converts videos with the next extensions: `mp4, avi, wmv, mkv, mpg`. If you want to add a new one, please add it in the method `has_ext`.
 - The variable `factor` indicates the quality of the resulting videos. Zero means the maximum quality, the greater the value the lesser quality the resulting videos will have.
 - The variable `ext` indicates the format of the resulting videos.