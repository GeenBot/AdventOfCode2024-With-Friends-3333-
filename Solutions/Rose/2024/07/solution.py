import sys
from itertools import product

def concat(a, b):
    if b < 10: return a * 10 + b
    if b < 100: return a * 100 + b
    if b < 1000: return a * 1000 + b
    if b < 10000: return a * 10000 + b

def match(t, ns, p2):
    n = len(ns) - 1
    ops = ["+", "*"]
    if p2: ops.append("||")

    for ops in product(ops, repeat=n):
        res = ns[0]
        for i in range(n):
            if ops[i] == "+":
                res += ns[i + 1]
            elif ops[i] == "*":
                res *= ns[i + 1]
            elif p2 and ops[i] == "||":
                res = concat(res, ns[i + 1])
                # res = int(f"{res}{ns[i + 1]}")
        if res == t:
            return True
    return False

def sol(d, p2):
    c = 0
    for l in d:
        t, ns = l.split(": ")
        t = int(t)
        ns = list(map(int, ns.split()))
        if match(t, ns, p2):
            c += t
    return c

with open(sys.argv[1]) as f:
    contents = f.readlines()
    print(sol(contents, False))
    print(sol(contents, True))
