#!/usr/bin/env python3

# clue 1
# change url to http://www.pythonchallenge.com/pc/def/banner.p

import pickle
import urllib3

http = urllib3.PoolManager()
url = "http://www.pythonchallenge.com/pc/def/banner.p"
r = http.request('GET', url)
data = pickle.loads(r.data)

for x in data:
    for y in x:
        print(y[0]*y[1],end='')
    print('')


# Ans = "channel"
# http://www.pythonchallenge.com/pc/def/channel.html
