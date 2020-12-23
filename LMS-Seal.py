from functions import *

# data and lines for testing
data = [(1.35, 5), (3.3, 5.3), (4.7, 4.3)]
lines = [[(1, 2), (3.5, 2.25)], [(3.5, 2.25), (4.75, 1)]]

InitialMove(data, lines)

startlnpt = lines[0][0][0]
endlnpt = lines[len(lines)-1][1][0]

linerange = endlnpt-startlnpt

n = 100
xerrors = [[0] for i in range(0, round(linerange*n))]

i = 0
while i < linerange*n:
    move(data, 1/n, 'x')
    xerrors[i] = GetXErrorAverage(data, lines)
    i = i+1

InitialMove(data, lines)

i = 0
minindex = 0
for i in range(len(xerrors)):
    if xerrors[i]< xerrors[minindex]:
        minindex = i

move(data, (1/n)*minindex, 'x')
print(data)

