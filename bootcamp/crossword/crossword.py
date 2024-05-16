w = 'w'
b = 'b'
def is_numbered(row_value: int, col_value: int, grid) -> bool:
    if grid[row_value][col_value] == 'w':
        if row_value == 0 and grid[row_value + 1][col_value] == 'w':
            return True 
        elif col_value == 0 and grid[row_value][col_value + 1] == 'w':
            return True 
        elif col_value > 0 and col_value < 14 and grid[row_value][col_value - 1] == 'b' and grid[row_value][col_value + 1] == 'w':
            return True
        elif row_value > 0 and row_value < 14 and grid[row_value - 1][col_value] == 'b' and grid[row_value + 1][col_value] == 'w':
            return True
    return False

        
def numbered_grid(grid):
    num = 1
    for row in range(15):
        for col in range(15):
            if is_numbered(row, col, grid):
                grid[row][col] = num
                num += 1
    return grid

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
print(numbered_grid(grid))