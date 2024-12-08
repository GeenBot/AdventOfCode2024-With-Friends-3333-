import sys
from collections import defaultdict

def get_cs(grid):
    cs = defaultdict(set)
    for r in range(len(grid)):
        for c in range(len(grid[r])):
            if grid[c][r] != ".":
                cs[grid[c][r]].add((c, r))
    return cs

def is_valid(r, c, grid):
    return 0 <= r < len(grid) and 0 <= c < len(grid[0])

def sol(grid, p2):
    cs = get_cs(grid)
    n = set()
    for c in cs.values():
        for y1, x1 in c:
            for y2, x2 in c:
                if (x1, y1) == (x2, y2):
                    continue

                dr = x1 - x2
                dc = y1 - y2

                if p2:
                    nr = x1
                    nc = y1

                    while is_valid(nr, nc, grid):
                        n.add((nr, nc))
                        nr += dr
                        nc += dc
                else:
                    nr = x1 + dr
                    nc = y1 + dc

                    if is_valid(nr, nc, grid):
                        n.add((nr, nc))
    return len(n)

with open(sys.argv[1]) as f:
    grid = [list(line.strip()) for line in f.readlines()]
    print(sol(grid, False))
    print(sol(grid, True))
