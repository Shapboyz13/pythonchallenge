import bz2, re, requests, ast, bz2

# <!--
# un: 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
# pw: 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'
# -->

url = requests.get('http://www.pythonchallenge.com/pc/def/integrity.html')
un = re.findall(r'un: \'(.*)\'',url.text)[0]
pw = re.findall(r'pw: \'(.*)\'',url.text)[0]

un = "'"+un+"'"
pw = "'"+pw+"'"

un = ast.literal_eval("b%s" % un)
pw = ast.literal_eval("b%s" % pw)

print ("UserName : ",bz2.decompress(un))
print ("passWord : ",bz2.decompress(pw))
