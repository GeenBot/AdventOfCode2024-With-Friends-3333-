from heapq import heappush, heappop
import sys

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def nbors(pos, size):
    x, y = pos
    nbors = []
    for dx, dy in DIRS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < size and 0 <= ny < size:
            nbors.append((nx, ny))
    return nbors

def find(c, size):
    start = (0, 0)
    t = (size - 1, size - 1)

    queue = [(dist(start, t), 0, start, [start])]
    v = set()

    while queue:
        _, cost, cur, path = heappop(queue)

        if cur == t:
            return len(path) - 1

        if cur in v:
            continue

        v.add(cur)

        for npos in nbors(cur, size):
            if npos not in v and npos not in c:
                npath = path + [npos]
                ncost = cost + 1
                priority = ncost + dist(npos, t)
                heappush(queue, (priority, ncost, npos, npath))
    return None

def solve(c, s=71, b=1024):
    c = set(c[:b])
    return find(c, s)

def find2(cs, s):
    low, high = 0, len(cs) - 1
    blocked = None

    while low <= high:
        mid = (low + high) // 2
        cx = set(cs[:mid+1])

        if find(cx, s) is None:
            blocked = cs[mid]
            high = mid - 1
        else:
            low = mid + 1

    return blocked

def solve2(c, s=71):
    b = find2(c, s)
    return f"{b[0]},{b[1]}"

with open(sys.argv[1]) as f:
    c = []

    for line in f:
        x, y = map(int, line.strip().split(','))
        c.append((x, y))

    print(solve(c))
    print(solve2(c))
