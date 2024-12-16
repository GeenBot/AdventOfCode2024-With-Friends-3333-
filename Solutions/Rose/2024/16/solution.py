from collections import defaultdict
from heapq import heappush, heappop
import sys

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def sol(grid, part2):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                start = (y, x)
            elif grid[y][x] == 'E':
                end = (y, x)

    pq = [(0, (start[0], start[1], 0))]
    dist = defaultdict(lambda: float('inf'))
    dist[(start[0], start[1], 0)] = 0
    pre = defaultdict(list)
    v = set()

    while pq:
        cost, (y, x, dir) = heappop(pq)

        if part2:
            if cost > dist[(y, x, dir)]:
                continue
        else:
            if (y, x, dir) in v:
                continue

            v.add((y, x, dir))
            if (y, x) == end:
                return cost

        for a in [1, -1]:
            ndir = (dir - a) % 4
            ncost = cost + 1000
            if ncost <= dist[(y, x, ndir)]:
                if ncost < dist[(y, x, ndir)]:
                    dist[(y, x, ndir)] = ncost
                    heappush(pq, (ncost, (y, x, ndir)))
                pre[(y, x, ndir)].append((y, x, dir))

        dy, dx = DIRS[dir]
        ny, nx = y + dy, x + dx

        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] != '#':
            ncost = cost + 1
            if ncost <= dist[(ny, nx, dir)]:
                if ncost < dist[(ny, nx, dir)]:
                    dist[(ny, nx, dir)] = ncost
                    heappush(pq, (ncost, (ny, nx, dir)))
                pre[(ny, nx, dir)].append((y, x, dir))

    ecost = float('inf')
    es = []
    for dir in range(len(DIRS)):
        if dist[(end[0], end[1], dir)] < ecost:
            ecost = dist[(end[0], end[1], dir)]
            es = [(end[0], end[1], dir)]
        elif dist[(end[0], end[1], dir)] == ecost:
            es.append((end[0], end[1], dir))

    tiles = set()
    ps = set(es)
    fps = set()

    while ps:
        current = ps.pop()
        if current in fps:
            continue

        fps.add(current)
        y, x, _ = current
        tiles.add((y, x))

        for prev in pre[current]:
            if dist[prev] + (1000 if prev[2] != current[2] else 1) == dist[current]:
                ps.add(prev)
    return len(tiles)

with open(sys.argv[1]) as f:
    grid = [line.strip() for line in f.readlines()]
    print(sol(grid, False))
    print(sol(grid, True))
