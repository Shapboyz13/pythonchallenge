from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
# or: requests.get(url).content

resp = urlopen("http://www.pythonchallenge.com/pc/def/channel.zip")
zipfile = ZipFile(BytesIO(resp.read()))

# shows name of all the files present in zip, where i found readme file
# for x in zipfile.namelist():
#     print (x)

# function to read lines from file.
# for line in zipfile.open('readme.txt').readlines():
#     print(line.decode('utf-8'))

# welcome to my zipped list.
# hint1: start from 90052
# hint2: answer is inside the zip


filename='90052.txt'
comment = []
while(filename):
    try:
        for line in zipfile.open(filename).readlines():
            print (line.decode('utf-8'))
            comment.append(zipfile.getinfo(filename).comment.decode('utf-8'))
            filename=line.decode('utf-8').split(' ')[-1]
            if not int(filename):
                filename = False;
            else:
                filename=filename + '.txt'
            print (filename)
    except ValueError:
        filename=False

# prints output nicely
for x in comment:
    print(x,end='')


# Ans="Hockey"
# ****************************************************************
# ****************************************************************
# **                                                            **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE NN      NN  **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE  NN    NN   **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE       NN  NN    **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE     NNNN     **
# **   OOOOOOOO XX    XX YY        GGG       EEEEE      NN      **
# **   OO    OO XXX  XXX YYY   YY  GG GG     EE         NN      **
# **   OO    OO  XXXXXX   YYYYYY   GG   GG   EEEEEE     NN      **
# **   OO    OO    XX      YYYY    GG    GG  EEEEEE     NN      **
# **                                                            **
# ****************************************************************
#  **************************************************************

# Ans = "oxygen"
