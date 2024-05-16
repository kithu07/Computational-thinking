from collections import defaultdict as ddict
SPACE, COMMENT = ' ', '#'


def load_data(filename: str) -> "dict[int, list[str]]":
    data = ddict(list)
    with open(filename) as f:
        for line in f:
            if line[0] != COMMENT:
                mark_start = line.rfind(SPACE)
                data[int(line[mark_start:])].append(line[:mark_start])
    return data


def make_ranklist(data: "dict[int, list[str]]") -> "list[str]":
    ranklist = []
    rank = 1
    for mark in sorted(data.keys(), reverse=True):
        for name in data[mark]:
            ranklist.append(f'{rank:4} {name:40} {mark:4}')
        rank += len(data[mark])
    return ranklist


for line in make_ranklist(load_data("marklist.txt")):
    print(line)
