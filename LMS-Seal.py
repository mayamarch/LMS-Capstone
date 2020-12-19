from PTL import *

# data and lines for testing
test_data = [(1.35, 5), (3.3, 5.3), (4.7, 4.3)]
test_lines = [[(1, 2), (3.5, 2.25)], [(3.5, 2.25), (4.75, 1)]]
n = 0.0001

InitialMove(test_data, test_lines)

xmax = Max(test_data, 'x')
print(xmax)

