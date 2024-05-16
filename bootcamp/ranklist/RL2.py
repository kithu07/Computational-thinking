from collections import defaultdict as ddict
SPACE, COMMENT = ' ', '#'


def load_data(filename: str) -> "dict[int, list[str]]":
    pass_data = ddict(list)
    fail_data = ddict(list)
    with open(filename) as f:
        for line in f:
            marklist = []
            if line[0] != COMMENT:
                for elem in line.split():
                    if elem.isdigit():
                        marklist.append(int(elem))
                totmark = sum(marklist)
                if all(mark > 40 for mark in marklist):
                    
                    pass_data[totmark].append(" ".join(f for f in line.split() if not f.isdigit()))
                else:
                    fail_data[totmark].append(line.split() - marklist)     
    return pass_data, fail_data
print(load_data("marklist.txt"))


def make_ranklist(pass_data: "dict[int, list[str]]", fail_data: "dict[int, list[str]]") -> "list[str]":
    pass_ranklist = []
    fail_ranklist = []
    rank = 1
    for totmark in sorted(data.keys(), reverse=True):
        for name in data[totmark]:
            pass_ranklist.append(f'{rank:4} {name:40} {mark:4}')
        rank += len(data[mark])
    return ranklist


for line in make_ranklist(load_data("marks.txt")):
    print(line)
