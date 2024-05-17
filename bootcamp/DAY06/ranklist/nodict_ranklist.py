SPACE, COMMENT = ' ', '#'


def parse(line: str) -> tuple[int, str]:
    line = line.strip()
    mark_start = line.rfind(SPACE)
    return int(line[mark_start:]), line[:mark_start].strip()


def load_data(filename: str) -> list[tuple[int, str]]:
    return [parse(line) for line in open(filename) if line[0] != COMMENT]


def make_ranklist(filename: str) -> list[str]:
    data = load_data(filename)
    marks = [mark for (mark, _) in data]

    def lookup(m: int) -> int:
        return 1 + len([mark for mark in marks if mark > m])
    return sorted([f'{lookup(mark):4} {name:40} {mark:4}'
                  for mark, name in data])


for line in make_ranklist("marks.txt"):
    print(line)
