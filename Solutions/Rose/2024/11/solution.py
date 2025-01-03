import sys
from collections import defaultdict, Counter

def blink(s):
    if s == 0:
        return [1]

    ss = str(s)
    l = len(ss)
    hl = l // 2

    if l % 2 == 0:
        return [int(ss[:hl]), int(ss[hl:])]
    else:
        return [2024 * s]

def zero():
    return 0

def sol(sc):
    nsc = Counter()

    for s, c in sc.items():
        for ns in blink(s):
            nsc[ns] += c

    return nsc

with open(sys.argv[1]) as f:
    ss = [int(num) for num in f.read().split()]
    sc = Counter(ss)

    for i in range(75):
        if i == 25:
            print(sum(x for x in sc.values()))
        sc = sol(sc)

    print(sum(x for x in sc.values()))
