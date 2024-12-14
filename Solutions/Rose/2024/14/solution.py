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

def s1(robots):
    ans = [0, 0, 0, 0]
    for (px, py), (vx, vy) in robots:
        nx, ny = px + 100 * vx, py + 100 * vy
        nx %= rows
        ny %= cols
        quad(nx, ny, ans)
    return ans[0] * ans[1] * ans[2] * ans[3]

def s2(robots):
    s = 0
    while True:
        grid = [[0 for _ in range(rows)] for _ in range(cols)]
        s += 1

        inv = False
        for (px, py), (vx, vy) in robots:
            nx, ny = px + s * vx, py + s * vy
            nx %= rows
            ny %= cols

            grid[ny][nx] += 1
            if grid[ny][nx] > 1:
                inv = True

        if not inv:
            # for row in grid:
            #     print("".join(map(str, row)).replace("0", "."))
            break
    return s

with open(sys.argv[1]) as f:
    c = f.readlines()
    robots = parse(c)
    print(s1(robots))
    print(s2(robots))
