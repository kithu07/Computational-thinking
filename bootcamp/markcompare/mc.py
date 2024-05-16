def topper_list_of2(A: str, marklistA: list, B: str, marklistB: list) -> list:
    list_of_toppers = []
    for markA, markB in zip(marklistA, marklistB):
        if markA >= markB:
            list_of_toppers.append(A)  
        else:
            list_of_toppers.append(B)
    return list_of_toppers
    
def scored_higher_than(A: str, marklistA: list, B: str, marklistB: list) -> str:
    if topper_list_of2(A, marklistA, B, marklistB) == [A] * len(marklistA):
        