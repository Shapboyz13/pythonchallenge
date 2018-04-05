#!/usr/bin/env python3

# clue 1
# change url to http://www.pythonchallenge.com/pc/def/linkedlist.php

import urllib3

http = urllib3.PoolManager()
url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345"
for i in range(400):
    r = http.request('GET', url)
    print (str(r.data))
    r = str(r.data).split()[-1]
    url="http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="+r


# Ans -
# got peak.html
# http://www.pythonchallenge.com/pc/def/peak.html
