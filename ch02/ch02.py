#!/usr/bin/python3

# from string import maketrans

# Clue1 = K -> M, O -> Q and E -> G

intab = "KOE"
outtab = "MQG"

transtab = str.maketrans(intab, outtab);
print(transtab);
transtab=str.maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab");
input_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(input_string.translate(transtab))

# clue2
# i hope you didnt translate it by hand. thats what computers are for. doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

print("map".translate(transtab));

# Ans:
# http://www.pythonchallenge.com/pc/def/ocr.html
