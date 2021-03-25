from Laser import *

laserdatatest = distance

minvalue = laserdatatest[0]
for i in range(0, len(laserdatatest)):
    if laserdatatest[i] < minvalue:
        minvalue = laserdatatest[i]

for i in range(0, len(laserdatatest)):
    if laserdatatest[i] == minvalue:
        print('Minimum Distance is at Interval:', i)

