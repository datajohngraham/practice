#!/usr/local/bin/python3
print("hi")
from collections import defaultdict
ocurrences = defaultdict(int)
with open(r'/users/abrick/resources/american-english-insane') as eng:
        for line in eng:
                for i in range(0,len(line)-2):
                        di = line[i:i+2].lower()
                        ocurrences[di] += 1
sl = sorted(ocurrences, key=lambda k: ocurrences[k], reverse=True)
for s in sl[:10]:
        print(s, ocurrences[s])
comb = []
for _ in [chr(i) for i in range(ord('a'), ord('z')+1)]:
        for __ in [chr(i) for i in range(ord('a'), ord('z')+1)]:
                comb.append(str(_) + str(__))
for up in comb:
        if up not in sl:
                print(up)
