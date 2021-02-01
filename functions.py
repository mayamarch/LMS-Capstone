import math


def dot(v, w):
    x, y = v
    X, Y = w
    return x * X + y * Y


def length(v):
    x, y = v
    return math.sqrt(x * x + y * y)


def vector(b, e):
    x, y = b
    X, Y = e
    return X - x, Y - y


def unit(v):
    x, y = v
    mag = length(v)
    return x / mag, y / mag


def distance(p0, p1):
    return length(vector(p0, p1))


def scale(v, sc):
    x, y = v
    return x * sc, y * sc


def add(v, w):
    x, y = v
    X, Y = w
    return x + X, y + Y


def pnt2line(pnt, start, end):
    line_vec = vector(start, end)
    pnt_vec = vector(start, pnt)
    line_len = length(line_vec)
    line_unitvec = unit(line_vec)
    pnt_vec_scaled = scale(pnt_vec, 1.0/line_len)
    t = dot(line_unitvec, pnt_vec_scaled)
    if t < 0.0:
        t = 0.0
    elif t > 1.0:
        t = 1.0
    nearest = scale(line_vec, t)
    dist = distance(nearest, pnt_vec)
    nearest = add(nearest, start)
    return dist, nearest


def Error(pnt, nearest):
    Error = abs((pnt-nearest)/nearest)
    return Error


def average(data):
    sum = 0
    for t in data:
        sum = sum + t

    avg = sum / len(data)
    return avg


def move(data, n, axis):
    if axis == 'x':
        for i in range(len(data)):
            data[i] = (data[i][0]+n, data[i][1])
    elif axis == 'y':
        for i in range(len(data)):
            data[i] = (data[i][0], data[i][1]+n)
    else:
        print('Axis value is not valid. Data has not been moved.')
    return data


def InitialMove(data, lines):
    x = lines[0][0][0] - data[0][0]
    y = lines[0][0][1] - data[0][1]
    move(data, x, 'x')
    move(data, y, 'y')
    return data


def Max(data, axis):
    if axis == 'x':
        n = 0
    elif axis == 'y':
        n = 1
    max = data[0][n]
    for i in range(0, len(data)):
        if data[i][n] > max:
            max = data[i][n]
    return max

class Result:

    def __init__(self, distance, coordinate):
        self.distance = distance
        self.coordinate = coordinate

def GetXErrorAverage(data, lines):
    # creating matrix of the values on the line segments that is closest each of the laserdata points
    test = []
    closest = []

    for i in range(0, len(data)):

        for j in range(0, len(lines)):
            distance, coordinate = pnt2line(data[i], lines[j][0], lines[j][1])
            test.append(Result(distance, coordinate))

        minimum = test[0].distance
        index = 0
        j = 0
        for result in test:
            if result.distance < minimum:
                minimum = result.distance
                index = j
            j += 1

        closest.append(test[index].coordinate)
        test.clear()

    xtest = [[0] for i in range(len(data))]
    for i in range(0, len(data)):
        xtest[i] = Error(data[i][0], closest[i][0])

    # averaging the error values
    xErrorAvg = average(xtest)

    return xErrorAvg

def GetYErrorAverage(data, lines):
    # creating matrix of the values on the line segments that is closest each of the laserdata points
    test = []
    closest = []

    for i in range(0, len(data)):

        for j in range(0, len(lines)):
            distance, coordinate = pnt2line(data[i], lines[j][0], lines[j][1])
            test.append(Result(distance, coordinate))

        minimum = test[0].distance
        index = 0
        j = 0
        for result in test:
            if result.distance < minimum:
                minimum = result.distance
                index = j
            j += 1

        closest.append(test[index].coordinate)
        test.clear()

    # creating list of the x error of each laserdata point and their corresponding "closest" value
    i = 0
    ytest = [[0] for i in range(len(data))]

    while i < len(data):
        ytest[i] = Error(data[i][1], closest[i][1])
        i = i + 1

    # averaging the error values
    yErrorAvg = average(ytest)

    return yErrorAvg
