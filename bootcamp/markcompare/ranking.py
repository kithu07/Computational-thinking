from itertools import combinations as nCr

COMMENT = "#"
LT, GT, NE = "<", ">", "#"

def load_data(filename: str) -> list[tuple[str, list[int]]]:
    data = list()
    with open(filename) as f:
        for line in f:
            if line[0] != COMMENT:
                name, *raw_marks = line.split()
                data.append((name, [int(r) for r in raw_marks]))
    return data


def relation(a_student: tuple[str, list[int]],
             b_student: tuple[str, list[int]]) -> tuple[str, str]:

    a_name, a_marks = a_student
    b_name, b_marks = b_student

    if all(a < b for (a, b) in zip(a_marks, b_marks)):
        return a_name, b_name
    elif all(a > b for (a, b) in zip(a_marks, b_marks)):
        return b_name, a_name


def all_relations(filename: str) -> list[str]:
    data = load_data(filename)
    relations = {relation(*pair) for pair in nCr(data, 2)}
    return {r for r in relations if r}


def redundancies(relations: list[str]) -> list[str]:
    firsts = {r[0] for r in relations}
    seconds = {r[-1] for r in relations}
    both = firsts & seconds
    redundancies = set()
    for f in firsts:
        for s in seconds:
            for b in both:
                if (f, s) in relations and\
                   (f, b) in relations and\
                   (b, s) in relations:
                    redundancies.add((f,s))
    return redundancies


relations = all_relations("studentRanking.txt")
duplicates = redundancies(relations)
irreducibles = relations - duplicates

print(relations)
print(duplicates)
print(irreducibles)

