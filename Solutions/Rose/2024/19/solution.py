import sys

def can_make(d, ps, memo=None):
    if memo is None:
        memo = {}

    if not d:
        return True

    if d in memo:
        return memo[d]

    for p in ps:
        if d.startswith(p):
            remaining = d[len(p):]
            if can_make(remaining, ps, memo):
                memo[d] = True
                return True

    memo[d] = False
    return False

def count_ways(d, ps, memo=None):
    if memo is None:
        memo = {}

    if d in memo:
        return memo[d]

    if not d:
        return 1

    ways = 0
    for p in ps:
        if d.startswith(p):
            remaining = d[len(p):]
            ways += count_ways(remaining, ps, memo)

    memo[d] = ways
    return ways

def s1(data):
    parts = data.strip().split('\n\n')
    ps = [p.strip() for p in parts[0].split(',')]
    ds = [d.strip() for d in parts[1].split('\n')]

    c = 0
    for d in ds:
        if can_make(d, ps):
            c += 1
    return c

def s2(data):
    parts = data.strip().split('\n\n')
    ps = [p.strip() for p in parts[0].split(',')]
    ds = [d.strip() for d in parts[1].split('\n')]

    c = 0
    for d in ds:
        c += count_ways(d, ps)
    return c

with open(sys.argv[1]) as f:
    c = f.read()
    print(s1(c))
    print(s2(c))
