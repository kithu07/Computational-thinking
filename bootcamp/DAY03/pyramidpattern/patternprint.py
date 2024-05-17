def symbols_inline(line_no: int) -> int:
    return '*' * (line_no * 2 - 1)
def print_pattern(lines_required: int) -> str:
    start = 40
    pattern = ""
    for i in range(1, lines_required+1):
        start -= 1 
        pattern += (' ' * start) + symbols_inline(i) + '\n' 
    return pattern
print(print_pattern(10))