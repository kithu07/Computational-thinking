def knight_moves(pos: str) ->list:
    possible_squares = []
    cols_index = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    index_cols = {v: k for k, v in cols_index.items()}

    col = cols_index[pos[0]]
    row = int(pos[1]) -1
    for row_jump in [-2, -1, 1, 2]:
        for col_jump in [-2, -1, 1, 2]:
            if abs(row_jump) != abs(col_jump) and 0 <= row + row_jump < 8 and 0 <= col + col_jump < 8:
                possible_squares.append(index_cols[col + col_jump] + str(row + row_jump + 1))
    return possible_squares
visited_boxes = []

def tour(pos: str) -> list :  
    visited_boxes.append(pos)
    possibilities = knight_moves(pos)
    if len(visited_boxes) == 64:
        return visited_boxes
    elif not possibilities:
        return visited_boxes
    else:
        for move in possibilities:
            if move not in visited_boxes:
                possibilities = tour(move)
        return visited_boxes  
    
print(tour('a1'))