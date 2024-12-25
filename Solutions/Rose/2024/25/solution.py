import sys

def can_fit(ls, ks):
    return not any(l == '#' and k == '#'
        for lr, kr in zip(ls, ks)
        for l, k in zip(lr, kr))

def solve(c):
    check = lambda i: [b.split('\n') for b in c.split('\n\n') if all(c == '#' for c in b.split('\n')[i])]
    ls = check(0)
    ks = check(-1)
    return sum(1 for l in ls for k in ks if can_fit(l, k))

with open(sys.argv[1]) as f:
    print(solve(f.read()))
