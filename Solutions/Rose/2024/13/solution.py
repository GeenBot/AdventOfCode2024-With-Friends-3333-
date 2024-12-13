import sys
import re

def parse(c, o):
    machines = []
    pattern = re.compile(r'Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)')

    for match in pattern.finditer(c):
        ax, ay, bx, by, px, py = map(int, match.groups())

        px += o
        py += o

        machines.append((ax, ay, bx, by, px, py))
    return machines

def sol(c, o):
    ms = parse(contents, o)
    c = 0

    for ax, ay, bx, by, px, py in ms:
        # basically solve
        # | ax  bx | | m |   | px |
        # | ay  by | | n | = | py |
        d1 = px * by - py * bx
        d2 = ax * by - ay * bx

        if d1 // d2 != d1 / d2:
            continue

        m = d1 // d2
        d3 = py - ay * m

        if d3 // by != d3 / by:
            continue

        n = (py - ay * m) // by
        c += 3 * m + n
    return c

with open(sys.argv[1]) as f:
    contents = f.read()
    print(sol(contents, 0))
    print(sol(contents, 10000000000000))
