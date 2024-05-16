def extract_data(filename: str) -> "list[tuple[int, str]]" :
    with open(filename) as f:
        data = []
        for line in f.readlines():
            *name, mark = line.split()
            data.append((mark, name))
    return data
print(extract_data("marklist.txt"))

def make_ranklist(filename: str) -> list[str]:
    data = extract_data(filename)
    