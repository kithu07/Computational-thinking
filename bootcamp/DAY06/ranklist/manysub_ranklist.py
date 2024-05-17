SPACE, COMMENT = ' ', '#'


def parse(line: str) -> "tuple[int, int, str, list[int]]":
    fields = line.strip().split()
    marks = [int(f) for f in fields if f.isdigit()]
    fails = len([mark < 40 for mark in marks])
    name = SPACE.join(f for f in fields if not f.isdigit())
    return fails, sum(marks), name, marks


def load_data(filename: str) -> "list[tuple[int, str]]":
    return [parse(line) for line in open(filename) if line[0] != COMMENT]


def make_ranklist(filename: str) -> "list[str]":
    ranklist = []
    data = sorted(load_data(filename), key=lambda rec: (rec[0], -rec[1]))
    rank = 0
    prev = 0
    for position, rec in enumerate(data, start=1):
        if rec[1] != prev:
            rank = position
            prev = rec[1]
        ranklist.append(f'{rank:4}{rec[1]:5}{rec[2]:40}{rec[3]}')
    return ranklist


for line in make_ranklist("studentmarks.txt"):
    print(line)
