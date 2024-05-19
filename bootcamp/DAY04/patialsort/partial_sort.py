data = [['A', 12, 14, 16],
 ['B', 5, 6, 7],
 ['C', 17, 20, 23],
 ['D', 2, 40, 12],
 ['E', 3, 41, 13],
 ['F', 7, 8, 9],
 ['G', 4, 5, 6]]

SHARP = "#"
LT = "<"

def changetodict(data):
    details = {}
    for d in data:
        details[d[0]] = d[1:]
    return details

data = changetodict(data)
print(data)
keys = list(data.keys())

def is_greater(stud1,stud2):

    return all(a>b for a,b in zip(stud1,stud2))

def is_smaller(stud1,stud2):
     
    return all(a<b for a,b in zip(stud1,stud2))

def swap(a,b):
    temp = keys[keys.index(a)]
    keys[keys.index(b)]= a
    keys[keys.index(a)] = b

 
def sorting(data):
    for i in range(0,len(keys)):
        for j in range(0,len(keys)):
            for std1,std2 in zip(keys[i], keys[j]):
                if is_greater(data[std1],data[std2]):
                    swap(std1,std2)
    return keys

keys = sorting(data)
def ranking(keys):
    ranks = ""
    for i,j in zip(keys,keys[1:]) :
        if is_smaller(data[i],data[j]):
            ranks += f"{i} {LT} "
        elif not is_greater(data[i],data[j]):
            ranks += f"{i} {SHARP} "
    ranks += keys[-1]
    return ranks
ranks = ranking(keys)
def final_ranks(ranks):
    comparable1,uncomparables,comparable2 = ranks.split(SHARP)
    return f"{comparable1}{LT}{comparable2}",uncomparables

#print(final_ranks(ranks))
ranks = final_ranks(ranks)
for i in ranks:
    print(i)