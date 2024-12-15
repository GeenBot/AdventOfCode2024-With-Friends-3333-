# https://i.imgur.com/ARMCVEV.png
from collections import Counter
from math import floor, sqrt
import sys

sys.set_int_max_str_digits(int(1e10));

def normal(s):
    if s == 0: return [1]

    ss = str(s)
    l = len(ss)
    hl = l // 2

    if l % 2 == 0:
        return [int(ss[:hl]), int(ss[hl:])]
    else:
        return [2024 * s]

def third_eye(s, mid):
    if s < mid:
        return []
    else:
        t = floor(sqrt(s) ** 3)
        return [t, t - 1, t - 2, t - 3]

def x(sc):
    nsc = Counter()
    for s, c in sc.items():
        for ns in normal(s):
            nsc[ns] += c
    return nsc

def y(sc):
    stones = sorted(sc.keys())
    mid = stones[len(stones) // 2]
    nsc = Counter()
    for s, c in sc.items():
        for ns in third_eye(s, mid):
            nsc[ns] += c
    return nsc

with open(sys.argv[1]) as f:
    ss = [int(num) for num in f.read().split()]
    sc = Counter(ss)
    for i in range(20):
        print(i, sum(sc.values()))
        sc = x(sc)
        sc = y(sc)
    print(sum(sc.values()))
