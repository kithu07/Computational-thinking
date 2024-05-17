import sys
LINEWIDTH = 40
STAR, SPACE = "*", " "
LF = "\n"
SHARP, USCORE, BS = "#", "_", "\b"

# START, REPEAT, LAST = STAR, SPACE + STAR, ""
START, REPEAT, LAST = SHARP, USCORE + USCORE, BS + SHARP


def pattern(size: int):
    return [line(i) for i in range(size)]


def line(line_num: int) -> str:
    return start(line_num) + repeat(line_num) + last(line_num)


def start(n: int) -> str:
    return START


def repeat(n: int) -> str:
    return REPEAT * n


def last(n: int) -> str:
    return LAST


def make_pyramid(size: int) -> str:
    return LF.join([line.center(LINEWIDTH) for line in pattern(size)])


def make_right(size: int) -> str:
    return LF.join([line.rjust(LINEWIDTH) for line in pattern(size)])


def make_arrow(size: int) -> str:
    base = pattern(size)
    arrow = base + base[::-1][1:]
    return LF.join([line.rjust(LINEWIDTH) for line in arrow])


def make_diamond(size: int) -> str:
    base = pattern(size)
    diamond = base + base[::-1][1:]
    return LF.join([line.center(LINEWIDTH) for line in diamond])


def make_hourglass(size: int) -> str:
    base = pattern(size)
    hourglass = base[::-1] + base[1:]
    return LF.join([line.center(LINEWIDTH) for line in hourglass])


for arg in sys.argv[1:]:
    size = int(arg)
    print(make_pyramid(size))
    #print(make_right(size))
    #print(make_arrow(size))
    #print(make_diamond(size))
    #print(make_hourglass(size))
