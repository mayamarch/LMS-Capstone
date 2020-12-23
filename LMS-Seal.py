from functions import *

# data and lines for testing
data = [(1.35, 5), (3.3, 5.3), (4.7, 4.3)]
lines = [[(1, 2), (3.5, 2.25)], [(3.5, 2.25), (4.75, 1)]]

# Move data to starting point of first line
InitialMove(data, lines)

# First and last lines
startlnpt = lines[0][0]
endlnpt = lines[len(lines)-1][1]

xlinerange = endlnpt[0]-startlnpt[0]

# Finding the X axis minimum error across length of seal
n = 1000
xerrors = [[0] for i in range(0, round(xlinerange*n))]

i = 0
while i < xlinerange*n:
    move(data, 1/n, 'x')
    xerrors[i] = GetXErrorAverage(data, lines)
    i = i+1

# Find the position of the min in xerrors
i = 0
xminindex = 0
for i in range(len(xerrors)):
    if xerrors[i]< xerrors[xminindex]:
        xminindex = i

# Move data back to original position
InitialMove(data, lines)

# Move data to position of min errror
move(data, (1/n)*xminindex, 'x')

print(data)

# Finding the Y axis minimum error across length of seal

ylinerange = 2
yerrors = [[0] for i in range(0, round(ylinerange*n))]

i = 0
while i < ylinerange*n:
    move(data, 1/n, 'y')
    yerrors[i] = GetYErrorAverage(data, lines)
    i = i+1

# Find the position of the min in yerrors
i = 0
yminindex = 0
for i in range(len(yerrors)):
    if yerrors[i]< yerrors[yminindex]:
        yminindex = i

# Move data back to original position
InitialMove(data, lines)

# Move data to position of xmin errror
move(data, (1/n)*xminindex, 'x')

# Move data to position of ymin errror
move(data, (1/n)*yminindex, 'y')

print(data)