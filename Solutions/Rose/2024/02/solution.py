import sys

def is_safe(r):
    diff = [r[i + 1] - r[i] for i in range(len(r) - 1)]

    inc = all(1 <= d <= 3 for d in diff)
    dec = all(-3 <= d <= -1 for d in diff)

    return inc or dec

def is_safe2(r):
    if is_safe(r):
        return True

    for i in range(len(r)):
        r2 = r[:i] + r[i + 1:]
        if is_safe(r2):
            return True

    return False

def sol(d, p2):
    c = 0

    for l in d.strip().split("\n"):
        r = list(map(int, l.split()))
        if is_safe2(r) if p2 else is_safe(r):
            c += 1

    return c

with open(sys.argv[1]) as f:
    d = f.read()
    print(sol(d, False))
    print(sol(d, True))
