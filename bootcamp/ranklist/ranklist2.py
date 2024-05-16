from collections import defaultdict as ddict
COMMENT = '#'

def extract_data(filename: str) -> "dict[int, list[str]]":
    data = ddict(list)
    with open(filename) as f:
        for line in f.readlines():
            if line[0] != COMMENT:
                mark_start = line.rfind(' ')
                data[int(line[mark_start:])].append(line[:mark_start])
    return data
print(extract_data("marklist.txt"))

def make_ranklist(filename: str) -> "list[str]":
    data = extract_data(filename)