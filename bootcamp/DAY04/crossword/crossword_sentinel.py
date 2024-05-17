import pprint
import sys

LF, BLACK, WHITE = '\n', '#', ''
gridfile = sys.argv[1]
DEBUG = len(sys.argv) == 3    #3 is an arbitary value, when it is passed, pprint gets executed

grid=[]
for line in open(sys.argv[1]):
    grid.append(line.strip(LF))
if DEBUG:
    pprint.pprint(grid)

size = len(grid)
grid.insert(0, BLACK * size)
grid.append(BLACK * size)
grid = [BLACK + line + BLACK for line in grid]

transpose=[]
for col in range(len(grid)):
    s = ""
    for row in grid:
        s += row[col]
    transpose.append(s)
if DEBUG:
    pprint