import sys
from typing import Counter

def do(secret, value):
    secret = secret ^ value
    return secret % 16777216

def next(secret):
    result = do(secret, secret * 64)
    result = do(result, result // 32)
    result = do(result, result * 2048)

    return result

def gen(secret, n):
    cur = secret
    for _ in range(n):
        cur = next(cur)
    return cur

def s1(c):
    secrets = [int(line.strip()) for line in c.split('\n') if line.strip()]

    total = 0
    for secret in secrets:
        total += gen(secret, 2000)

    return total

def s2(c):
    secrets = [int(line.strip()) for line in c.split('\n') if line.strip()]
    ps = []
    cs = []
    vs = Counter()

    for s in secrets:
        pl = []
        pc = []
        n = s

        for _ in range(2000):
            n = next(n)
            pl.append(n % 10)

            if len(pl) > 1:
                pc.append(pl[-1] - pl[-2])
        ps.append(pl)
        cs.append(pc)

    for i, pc in enumerate(cs):
        v = set()

        for j in range(3, len(pc)):
            t = tuple(pc[j - 3:j + 1])

            if t not in v:
                vs[t] += ps[i][j + 1]
                v.add(t)

    return max(vs.values())

with open(sys.argv[1]) as f:
    c = f.read()
    print(s1(c))
    print(s2(c))
