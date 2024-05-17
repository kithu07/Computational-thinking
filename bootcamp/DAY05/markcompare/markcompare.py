COMMENT = '#'
def load_data(filename: str) -> dict[str, list[int]]:
    data = dict()
    with open(filename) as f:
        for line in f:
            if line[0] != COMMENT:
                name, *raw_marks = line.split()
                data[name] = [int(r) for r in raw_marks]
    return data
         
def submarks_compare(A: str, marklistA: list, B: str, marklistB: list) -> list:    #better approach: use all()
    list_of_toppers = []
    for markA, markB in zip(marklistA, marklistB):
        if markA >= markB:
            list_of_toppers.append(A)  
        else:
            list_of_toppers.append(B)
    return list_of_toppers
    
def relaton(A: str, marklistA: list, B: str, marklistB: list) -> str:
    if submarks_compare(A, marklistA, B, marklistB) == [A] * len(marklistA):
        return A + '>' + B
    elif submarks_compare(A, marklistA, B, marklistB) == [B] * len(marklistA):
        return B + '>' + A
    else:
        return A + '#' + B
    
def all_relation(marksheet: dict):
    compare_list = []
    for student1 in list(marksheet):
        for student2 in list(marksheet)[list(marksheet).index(student1) + 1: ]:
            compare_list. append(relaton(student1, marksheet[student1], student2, marksheet[student2]))
    return compare_list

#def allrelations(filename:str) -> list[str]:
    data = load_data(filename)
    pairs = nCr(data.keys(), 2)
    #return {f'{pair[0]}{relation(data[pair[0]], data[] for pair in pairs}



print (all_relation({'A': [98,99,67], 'B': [88,78,55], 'C': [18,10,46], 'D': [22, 44, 82], 'E': [3, 41, 13], 'F': [7, 8, 9], 'G': [4, 5, 6]}))