w = 'w'
b = 'b'
def is_numbered(row_value: int, col_value: int, grid: list) -> bool:
    if grid[row_value][col_value] == 'w':
        if row_value == 0 and grid[row_value + 1][col_value] == 'w':
            return True 
        elif col_value == 0 and grid[row_value][col_value + 1] == 'w':
            return True 
        elif col_value > 0 and col_value < len(grid)-1 and grid[row_value][col_value - 1] == 'b' and grid[row_value][col_value + 1] == 'w':
            return True
        elif row_value > 0 and row_value < len(grid)-1 and grid[row_value - 1][col_value] == 'b' and grid[row_value + 1][col_value] == 'w':
            return True
    return False


def grid_of_tuples(grid: list) -> list: 
    numbered_grid = []
    num = 1
    for i in range(len(grid)):
        for j in range(len(grid)):
            if is_numbered(i,j, grid):
                numbered_grid.append((i, j, num))
                num += 1
    return numbered_grid

grid = [[w, w, w, w, w, w, b, w, w, w, w, w, w, w, w],
[w, b, w, b, w, b, w, b, w, b, w, b, w, b, w],
[w, w, w, w, w, w, w, w, w, b, w, w, w, w, w], 
[w, b, w, b, w, b, w, b, w, b, w, b, w, b, w],
[w, w, w, w, w, b, w, w, w, w, w, w, w, w, w],
[w, b, w, b, b, b, w, b, w, b, w, b, w, b, w],
[w, w, w, w, w, w, w, b, w, w, w, w, b, b, b],
[w, b, w, b, w, b, b, b, b, b, w, b, w, b, w],
[b, b, b, w, w, w, w, b, w, w, w, w, w, w, w],
[w, b, w, b, w, b, w, b, w, b, b, b, w, b, w],
[w, w, w, w, w, w, w, w, w, b, w, w, w, w, w],
[w, b, w, b, w, b, w, b, w, b, w, b, w, b, w],
[w, w, w, w, w, b, w, w, w, w, w, w, w, w, w],
[w, b, w, b, w, b, w, b, w, b, w, b, w, b, w], 
[w, w, w, w, w, w, w, w, b, w, w, w, w, w, w]]
print(grid_of_tuples(grid))