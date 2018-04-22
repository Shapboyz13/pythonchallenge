from PIL import Image
import numpy as np
from urllib.request import urlopen
import re

resp = urlopen("http://www.pythonchallenge.com/pc/def/oxygen.png")
img = Image.open(resp)
arr = np.array(img)

# clue 1 grayscale image in between
# clue 2 7 written on Image
# as soon as i converted image in list of coordinates and RGB color,
# i checked the height of image, so i can check pixel postion on grayscale line
#height of image is 95, half of which is 47.5, which by rounding the image pixel height to 7 i got below array.
# i am using row number 46

out=[]
for x in range(0,len(arr[46]),7):
    out.append(chr(arr[46][x][0]))

out = ''.join(out).rstrip('jld');
# output:- smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]jld
# jld is from last three pixels

out = re.findall(r"\['?([^'\]]+)'?\]", out)
out = out[0].split(', ')

for x in out:
    print(chr(int(x)),end="")

print()

# output : = integrity
# Ans:-http://www.pythonchallenge.com/pc/def/integrity.html
