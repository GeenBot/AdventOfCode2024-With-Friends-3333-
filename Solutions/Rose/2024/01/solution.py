import sys
from collections import Counter

def lists(x):
    ls = []
    rs = []

    with open(x, 'r') as file:
        for line in file:
            l, r = map(int, line.split())
            ls.append(l)
            rs.append(r)

    return (ls, rs)

ls, rs = lists(sys.argv[1])

def s1():
    lss = sorted(ls)
    rss = sorted(rs)
    dist = sum(abs(l - r) for l, r in zip(lss, rss))
    return dist

def s2():
    rsc = Counter(rs)
    score = sum(x * rsc[x] for x in ls)
    return score

print(s1())
print(s2())
