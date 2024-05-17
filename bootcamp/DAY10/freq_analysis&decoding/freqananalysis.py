from collections import defaultdict as ddict
import sys

freq = dict()
for i, arg in enumerate(sys.argv[1:]):
    for ch in open(arg).read():
        if ch not in freq:
            freq[ch] = [0,0,0]
        freq[chr[i]] += 1

for ch in freq:
    print(f'{freq[ch][0]:3} {freq[ch][1]:3} {freq[ch][2]:3}')