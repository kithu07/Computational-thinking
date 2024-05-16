def make_pairs(s: str):
    return zip(s, s[1:])

def encode(s: str) ->str:
    def encode_pair(pair: tuple[str, str]) ->str:
        if pair[0] < pair[1]:
            return 'A'
        elif pair[0] > pair[1]:
            return 'D'
        else:
            return 'E'
    return ''.join([encode_pair(_) for _ in make_pairs(s)])

def squeeze(s: str) ->str:
    if len(s) == 1:
        return s
    elif s[0] == s[1]:
        return squeeze((s[1:]))
    else:
        return squeeze(s[0] + s[1:])
    
def classify(s: str):
    rep = squeeze(encode(s))
    reps = {'A': 'A', 'D': 'D', 'AD': 'P', 'DA': 'V'}
    if rep not in reps:
        return 'X'
    else:
        return reps[rep]

COMMA = ','
for line in open("test_adpvx.txt"):
    data, answer = line.strip().split(COMMA)
    result = classify(data)
    if result == answer.strip():
        print(f'Works for {data}. Answer is {}')        

        

