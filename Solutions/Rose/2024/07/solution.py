from itertools import product

def match(t, ns):
    n = len(ns) - 1
    for ops in product(["+", "*"], repeat=n):
        res = ns[0]
        for i in range(n):
            if ops[i] == "+":
                res += ns[i + 1]
            elif ops[i] == "*":
                res *= ns[i + 1]
        if res == t:
            return True
    return False

def match2(t, ns):
    n = len(ns) - 1
    for ops in product(["+", "*", "||"], repeat=n):
        res = ns[0]
        for i in range(n):
            if ops[i] == "+":
                res += ns[i + 1]
            elif ops[i] == "*":
                res *= ns[i + 1]
            elif ops[i] == "||":
                res = int(f"{res}{ns[i + 1]}")
        if res == t:
            return True
    return False

def s1(d):
    c = 0
    for l in d:
        t, ns = l.split(": ")
        t = int(t)
        ns = list(map(int, ns.split()))
        if match(t, ns):
            c += t
    return c

def s2(d):
    c = 0
    for l in d:
        t, ns = l.split(": ")
        t = int(t)
        ns = list(map(int, ns.split()))
        if match2(t, ns):
            c += t
    return c

with open("input.txt") as f:
    contents = f.readlines()
    print(s1(contents))
    print(s2(contents))
