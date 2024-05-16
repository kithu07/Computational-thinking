LINEWIDTH = 40
SPACE = ' '
LF = '\n'
STAR = '*'
USCORE, HASH, BS = '_', '#', '\b'
 

START, REPEAT, LAST = HASH, USCORE + USCORE, BS + HASH

def line(line_num: int) -> str:
    return start(line_num) + repeat(line_num) + last(line_num)

def start(n: int) -> str:
    return START

def repeat(n: int) -> str:
    return REPEAT * n

def last(n: int) -> str:
    return LAST

def pattern(size: int):
    return[line(i) for i in range(size)]

#def line(line_num: int) -> str:
    return (2 * line_num + 1) * STAR

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

print(make_pyramid(4))
