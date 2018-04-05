#!/usr/bin/env python3

import urllib3
import re

http = urllib3.PoolManager()
url="http://www.pythonchallenge.com/pc/def/equality.html"
r = http.request('GET', url)
r = str(r.data)
r = r.split('<!--')[1]
re = re.compile('[^A-Z][A-Z]{3}[a-z][A-Z]{3}[^A-Z]')
data = re.findall(r)
print (''.join(x[4] for x in data))


# Ans - linkedlist
# http://www.pythonchallenge.com/pc/def/linkedlist.html
