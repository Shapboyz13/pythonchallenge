#!/usr/bin/python3

# clue1
# recognize the characters. maybe they are in the book,
# but MAYBE they are in the page source.
# inspect webpage
# we need to find
# find rare characters in the mess below:

import re

search_pattern = re.compile('[^\w]{2}[a-z][^\w]{2}')
with open ('ocr.html') as f:
    lines = f.read()
    str = search_pattern.findall(lines)
    print (''.join([x[2] for x in str]))


# ans = equality
# http://www.pythonchallenge.com/pc/def/equality.html
