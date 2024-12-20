from collections import deque
import sys

DIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
P1, P2 = 2, 20

def parse(c):
    grid = [list(line) for line in c.strip().split('\n')]
    start = end = None
    ws = set()

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == 'S':
                start = (y, x)
                grid[y][x] = '.'
            elif grid[y][x] == 'E':
                end = (y, x)
                grid[y][x] = '.'
            elif grid[y][x] == '#':
                ws.add((y, x))

    return grid, start, end, ws

def dists(grid, sy, sx, ws):
    rows, cols = len(grid), len(grid[0])
    queue = deque([(0, sy, sx)])
    v = set()
    ds = {}

    while queue:
        d, y, x = queue.popleft()
        if (y, x) in v:
            continue

        v.add((y, x))
        ds[(y, x)] = d

        for dx, dy in DIRS:
            ny, nx = (y + dx, x + dy)
            if 0 <= ny < rows and 0 <= nx < cols and (ny, nx) not in ws and (ny, nx) not in v:
                queue.append((d + 1, ny, nx))
    return ds

def get_ss(grid, sdists, edists, ws, btime):
    rows, cols = len(grid), len(grid[0])
    s1 = s2 = 0

    for sy in range(rows):
        for sx in range(cols):
            if (sy, sx) in ws or (sy, sx) not in sdists:
                continue

            queue = deque([(sy, sx, 0)])
            v = set()

            while queue:
                y, x, steps = queue.popleft()

                if steps > P2:
                    continue

                if (y, x) not in ws and (y, x) in edists:
                    total = sdists[(sy, sx)] + steps + edists[(y, x)]

                    if total < btime:
                        s = btime - total

                        if s >= 100:
                            if steps <= P1:
                                s1 += 1
                            if steps <= P2:
                                s2 += 1

                for dy, dx in DIRS:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < rows and 0 <= nx < cols and (ny, nx) not in v:
                        v.add((ny, nx))
                        queue.append((ny, nx, steps + 1))

    return s1, s2

def find_cheats(grid, sy, sx, ey, ex, ws):
    sdists = dists(grid, sy, sx, ws)
    edists = dists(grid, ey, ex, ws)
    btime = sdists.get((ey, ex), float("inf"))
    return get_ss(grid, sdists, edists, ws, btime)

with open(sys.argv[1]) as f:
    grid, (sy, sx), (ey, ex), ws = parse(f.read())
    s1, s2 = find_cheats(grid, sy, sx, ey, ex, ws)
    print(s1)
    print(s2)
