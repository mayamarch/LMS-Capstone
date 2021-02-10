from functions import *


def laser_algorithm(data, lines):
    f = open('laserdata.txt', 'r')
    ol_data = f.readlines()

    # Create (x,y), (x,y) list format
    laserdata = []
    for i in range(0, len(ol_data)):
        line = ol_data[i]
        values = line.split()
        laserdata.append((float(values[0]), float(values[1])))

    # Move laserdata to starting point of first line
    InitialMove(laserdata, lines)

    # First and last lines
    startlnpt = lines[0][0]
    endlnpt = lines[len(lines)-1][1]

    xlinerange = endlnpt[0]-startlnpt[0]

    # Finding the X axis minimum error across length of seal
    n = 1000
    xerrors = [[0] for i in range(0, round(xlinerange*n))]

    i = 0
    while i < xlinerange*n:
        move(laserdata, 1 / n, 'x')
        xerrors[i] = GetXErrorAverage(laserdata, lines)
        i = i+1

    # Find the position of the min in xerrors
    i = 0
    xminindex = 0
    for i in range(len(xerrors)):
        if xerrors[i]< xerrors[xminindex]:
            xminindex = i

    # Move laserdata back to original position
    InitialMove(laserdata, lines)

    # Move laserdata to position of min errror
    move(laserdata, (1 / n) * xminindex, 'x')


    # Find min/max y range
    y_min = lines[0][0][1]
    y_max = lines[0][0][1]
    for line in lines:
        for point in line:
            if point[1] < y_min:
                y_min = point[1]
            if point[1] > y_max:
                y_max = point[1]

    ylinerange = y_max - y_min

    # Finding the Y axis minimum error across height of seal
    yerrors = [[0] for i in range(0, round(ylinerange*n))]

    i = 0
    while i < ylinerange*n-1:
        move(laserdata, 1 / n, 'y')
        yerrors[i] = GetYErrorAverage(laserdata, lines)
        i = i+1

    # Find the position of the min in yerrors
    i = 0
    yminindex = 0
    for i in range(len(yerrors)):
        if yerrors[i] < yerrors[yminindex]:
            yminindex = i

    # Move laserdata back to original position
    InitialMove(laserdata, lines)

    # Move laserdata to position of xmin errror
    move(laserdata, (1 / n) * xminindex, 'x')

    # Move laserdata to position of ymin errror
    move(laserdata, (1 / n) * yminindex, 'y')

    # Getting x and y column for dearpygui
    laserdatax = []
    for i in range(0, len(laserdata)):
        laserdatax.append(laserdata[i][0])

    laserdatay = []
    for i in range(0, len(laserdata)):
        laserdatay.append(laserdata[i][1])

    return laserdatax, laserdatay, laserdata
