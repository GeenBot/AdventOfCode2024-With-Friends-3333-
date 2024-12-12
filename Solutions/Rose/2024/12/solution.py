import sys

def sol(grid, part2):
    ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    res = 0
    rs = {}
    v = set()

    def dfs(r, c, p):
        a = set()
        stack = [(r, c)]

        while stack:
            x, y = stack.pop()

            if (x, y) in v or x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]) or grid[x][y] != p:
                continue

            v.add((x, y))
            a.add((x, y))

            for nx, ny in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (nx, ny) not in v:
                    stack.append((nx, ny))
        return a

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if (r, c) not in v:
                area = dfs(r, c, grid[r][c])
                if grid[r][c] not in rs:
                    rs[grid[r][c]] = []
                rs[grid[r][c]].append(area)

    for areas in rs.values():
        for area in areas:
            bc = 0
            sc = 0

            for p in area:
                for d in [(p[0] + dx, p[1] + dy) for dx, dy in ds]:
                    if d not in area: bc += 1

            for d in ds:
                s = set()
                for p in area:
                    x = p[0] + d[0], p[1] + d[1]
                    if x not in area: s.add(x)

                rs = set()
                for p in s:
                    x = p[0] + d[1], p[1] + d[0]
                    while x in s:
                        rs.add(x)
                        x = x[0] + d[1], x[1] + d[0]
                sc += len(s) - len(rs)

            res += len(area) * (sc if part2 else bc)
    return res

with open(sys.argv[1]) as f:
    contents = f.read()
    grid = [list(row) for row in contents.split('\n') if row.strip()]
    print(sol(grid, False))
    print(sol(grid, True))
