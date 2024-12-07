import sys

contents = open(sys.argv[1]).read()
rd, ud = contents.split('\n\n')
rs = [tuple(map(int, r.split('|'))) for r in rd.splitlines()]
us = [list(map(int, u.split(','))) for u in ud.splitlines()]

def is_ordered(u):
    for x, y in rs:
        if x in u and y in u:
            if u.index(x) > u.index(y):
                return False
    return True

def reorder(u):
    while True:
        s = False
        for i in range(len(u) - 1):
            x, y = u[i], u[i + 1]
            for rx, ry in rs:
                if x == rx and y == ry:
                    u[i], u[i + 1] = u[i + 1], u[i]
                    s = True
                    break
        if not s:
            break
    return u

def s1():
    res = []

    for u in us:
        if is_ordered(u):
            mid = len(u) // 2
            res.append(u[mid])

    return sum(res)

def s2():
    res = []

    for u in us:
        if not is_ordered(u):
            u2 = reorder(u)
            mid = len(u2) // 2
            res.append(u2[mid])

    return sum(res)

print(s1())
print(s2())
