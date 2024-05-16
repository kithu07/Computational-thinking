s = "7x^5 + 6x^4 -3x^2 + 7"
def split_terms(s: str):
    if s[0] != '-':
        s = '+' + s
    for index, chr in enumerate(s):
        if chr == '-':
            s = s[: index ] + '+' + s[index: ] 
    return s.split( '+' )

def convert (s: str) -> str:
    list_terms = [i for i in split_terms( s ) if i != '']
    converted = "" 
    for i in list_terms[:: -1]:
        if i[0] != '-' :
            converted += '+' + i
        else:
            converted += i
    converted.replace(" ", "")
    return converted
print(convert(s))



    

