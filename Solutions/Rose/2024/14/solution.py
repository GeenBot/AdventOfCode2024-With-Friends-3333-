import sys

rows = 101
cols = 103

def parse(c):
    robots = []

    for line in [line for line in c if line.strip() != ""]:
        p, v = line.split()
        px, py = map(int, p[2:].split(","))
        vx, vy = map(int, v[2:].split(","))
        robots.append(((px, py), (vx, vy)))

    return robots

def quad(nx, ny, ans):
    if nx == rows // 2 or ny == cols // 2:
        return
    if nx < rows // 2 and ny < cols // 2:
        ans[0] += 1
    elif nx > rows // 2 and ny < cols // 2:
        ans[1] += 1
    elif nx < rows // 2 and ny > cols // 2:
        ans[2] += 1
    else:
        ans[3] += 1

def sol(robots):
    s = 0
    ans = [0, 0, 0, 0]
    while True:
        grid = [[0 for _ in range(rows)] for _ in range(cols)]
        s += 1

        inv = False
        for (px, py), (vx, vy) in robots:
            nx, ny = px + s * vx, py + s * vy
            nx %= rows
            ny %= cols

            if s == 100: quad(nx, ny, ans)

            grid[ny][nx] += 1
            if grid[ny][nx] > 1:
                inv = True
        if s == 100: print(ans[0] * ans[1] * ans[2] * ans[3])

        if not inv:
            # for row in grid:
            #     print("".join(map(str, row)).replace("0", "."))
            break
    return s

with open(sys.argv[1]) as f:
    c = f.readlines()
    robots = parse(c)
    print(sol(robots))
