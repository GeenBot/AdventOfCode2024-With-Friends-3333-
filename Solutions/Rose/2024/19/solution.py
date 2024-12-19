import sys

memo = {}
def count_ways(d, ps):
    if d in memo:
        return memo[d]

    if not d:
        return 1

    ways = 0
    for p in ps:
        if d.startswith(p):
            remaining = d[len(p):]
            ways += count_ways(remaining, ps)

    memo[d] = ways
    return ways

with open(sys.argv[1]) as f:
    parts = f.read().strip().split('\n\n')
    ps = [p.strip() for p in parts[0].split(',')]
    ds = [d.strip() for d in parts[1].split('\n')]

    c1 = c2 = 0
    for d in ds:
        res = count_ways(d, ps)
        c1 += not not res
        c2 += res
    print(c1)
    print(c2)
