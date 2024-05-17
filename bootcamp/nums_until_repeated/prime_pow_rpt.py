from sys import argv
def generate_mod():
    p = int(argv[1])
    b = bpow = int(argv[2])
    mods = []
    for i in range(1, p):
       # print(bpow, end=',')
        mods.append(bpow)
        bpow = (b* bpow) % p
    return mods

def count_before_rpt(mods: list):
    count = 0
    for i in mods:
        if i in mods[: i]:
            return mods.index(i)


print(count_before_rpt(generate_mod()))

         
