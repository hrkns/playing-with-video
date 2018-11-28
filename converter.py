import time
import winsound
from os import listdir
from os.path import isfile, join
mypath = "./"

def find_str(s, char):
  index = 0
  if char in s:
    c = char[0]
    for ch in s:
      if ch == c:
        if s[index:index+len(char)] == char:
          return index
      index += 1
  return -1

def has_ext(f):
	cond = False
	cond = cond or find_str(f, ".mp4") == len(f) - 4
	cond = cond or find_str(f, ".avi") == len(f) - 4
	cond = cond or find_str(f, ".wmv") == len(f) - 4
	cond = cond or find_str(f, ".mkv") == len(f) - 4
	cond = cond or find_str(f, ".mpg") == len(f) - 4
	return cond
  
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f)) and has_ext(f)]

from subprocess import call
counter = 0

for file in onlyfiles:
	print ("******************************************************************")
	print ("******************************************************************")
	print ("******************************************************************")
	print ("******************************************************************")
	print ("******************************************************************")
	print ("###FILE #" + str(counter))
	ext = ".mp4"
	newname = file[:len(file)-4]+ext;
	factor = str(0)

	if not isfile(join(mypath, newname)):
		call(["ffmpeg", "-i", ""+file+"", "-q:v", factor, newname])
	else:
		append = ''

		if (counter < 10):
			append = '0'

		while isfile(join(mypath, append + str(counter) + ext)):
			counter = counter + 1

			if counter >= 10:
				append = ''

		call(["ffmpeg", "-i", ""+file+"", "-q:v", factor, str(counter) + ext])

	counter = counter + 1
"""
while True:
	winsound.PlaySound("done.mp3", winsound.SND_ASYNC | winsound.SND_ALIAS )
	time.sleep(0.5)
"""
