# http://www.pythonchallenge.com/pc/return/cave.jpg

import numpy as np
from PIL import Image,ImageDraw

im = Image.open('cave.jpg')
(w, h) = im.size

even = Image.new('RGB', (w // 2, h // 2))
odd = Image.new('RGB', (w // 2, h // 2))

for i in range(w):
    for j in range(h):
        p = im.getpixel((i,j))
        if (i+j)%2 == 1:
            odd.putpixel((i // 2, j // 2), p)
        else:
            even.putpixel((i // 2, j // 2), p)

odd.show()
even.show()


# ANS:evil
