# on the click of image, it will redirect to new page
# with below info.
# a = [1, 11, 21, 1211, 111221,

# this sequence is know as Look-and-say sequence in mathmeticsself.

# Hint : len(a[30])=?

from itertools import groupby
# [len(list(group)) for key, group in groupby(a)]

for x in range(31):
    if x==0:
        number=[1]
        print (number)
    else:
        newNumber = []
        group = [len(list(group)) for key, group in groupby(number)]
        keys = [key for key, group in groupby(number)]
        for x in range(len(group)):
            newNumber.append(group[x])
            newNumber.append(keys[x])
        print (len(newNumber))
        number = newNumber;


# Ans: 5808
