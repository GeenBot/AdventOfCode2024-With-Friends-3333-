import sys

grid = []
x = y = sx = sy = dir = 0
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for line in open(sys.argv[1]).readlines():
    if "^" in line:
        y = len(grid)
        x = line.find("^")
        line = line.replace("^", "X")
        sy, sx = y, x
    grid.append([c for c in line])

def loop(cx, cy):
    visited = set()
    y, x, rows, cols, dir = sy, sx, len(grid), len(grid[0]), 0

    while True:
        state = (y, x, dir)

        if state in visited:
            return True
        visited.add(state)

        ny, nx = y + dirs[dir][0], x + dirs[dir][1]

        if not (0 <= ny < rows and 0 <= nx < cols):
            return False

        if grid[ny][nx] == '#' or (ny == cy and nx == cx):
            dir = (dir + 1) % len(dirs)
        else:
            y, x = ny, nx

def s1():
    global x, y, dir

    while True:
        if y + dirs[dir][0] < 0 or y + dirs[dir][0] >= len(grid) or x + dirs[dir][1] < 0 or x + dirs[dir][1] >= len(grid[0]):
            break

        if grid[y + dirs[dir][0]][x + dirs[dir][1]] == '#':
            dir = (dir + 1) % len(dirs)
        else:
            y += dirs[dir][0]
            x += dirs[dir][1]
            grid[y][x] = 'X'

    return sum(row.count('X') for row in grid)

def s2():
    s1()
    c = 0

    for ri, row in enumerate(grid):
        for ci, col in enumerate(row):
            if ri == sy and ci == sx:
                continue
            if col == 'X' and loop(ci, ri):
                c += 1

    return c

print(s1())
print(s2())
