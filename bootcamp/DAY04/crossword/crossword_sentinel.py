from pprint import pprint
BLACK, WHITE = 'b', 'w'

def load_grid() -> list:
    return [line.strip() for line in open("crossword_data.txt")]
    
def add_border(grid: list) -> list:
    size = len(grid)
    grid.insert(0, BLACK * size)
    grid.append(BLACK * size)
    return [BLACK + row + BLACK for row in grid]

def transpose_grid(grid: list) -> list:
    return [''.join(row) for row in zip(grid)]

def get_across(grid: list):
    size = len(grid)
    across = ''.join(grid)
    across_indices = []
    index = 0
    while index != -1:
        index = across.find(BLACK + WHITE + WHITE, index+ 1)
        if index != -1:
            across_indices.append(index)
    return {(pos//size, pos % size + 1) for pos in across_indices}

def get_down(transpose: list) -> set:
    size = len(transpose)
    down = ''.join(transpose)
    down_indices = []
    index = 0
    while index != -1:
        index = down.find(BLACK + WHITE + WHITE, index+ 1)
        if index != -1:
            down_indices.append(index)
    return {(pos % size + 1, pos // size) for pos in down_indices}


grid = add_border(load_grid())
transpose = transpose_grid(grid)

across_indexes = get_across(grid)
down_indexes = get_down(transpose)

print(list(enumerate(sorted(across_indexes | down_indexes), 1)))