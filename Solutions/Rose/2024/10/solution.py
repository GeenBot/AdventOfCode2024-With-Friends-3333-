import sys

def find(map):
    ts = []
    for row in range(len(map)):
        for col in range(len(map[0])):
            if map[row][col] == 0:
                ts.append((row, col))
    return ts

def do(map, start):
    rows, cols = len(map), len(map[0])
    stack = [start]
    ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    r9 = set()

    while stack:
        x, y = stack.pop()

        if map[x][y] == 9:
            r9.add((x, y))

        for dx, dy in ds:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if map[nx][ny] == map[x][y] + 1:
                    stack.append((nx, ny))

    return len(r9)

def s1(map):
    ts = find(map)
    c = 0

    for t in ts:
        s = do(map, t)
        c += s

    return c

def do2(map, start):
    rows, cols = len(map), len(map[0])
    stack = [(start, [start])]
    ds = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    r9 = set()

    while stack:
        (x, y), p = stack.pop()

        if map[x][y] == 9:
            r9.add(tuple(p))
            continue

        for dx, dy in ds:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if map[nx][ny] == map[x][y] + 1:
                    if (nx, ny) not in p:
                        stack.append(((nx, ny), p + [(nx, ny)]))

    return len(r9)

def s2(map):
    ts = find(map)
    c = 0

    for t in ts:
        s = do2(map, t)
        c += s

    return c

with open(sys.argv[1]) as f:
    map = [list(map(int, line)) for line in f.read().strip().split("\n")]
    print(s1(map))
    print(s2(map))
