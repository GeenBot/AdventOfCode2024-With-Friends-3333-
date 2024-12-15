import sys

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
OPTS = [">", "<", "v", "^"]

def parse(c):
    parts = c.strip().split('\n\n')
    l = parts[0].split("\n")
    ms = [DIRS[OPTS.index(m)] for m in parts[1].replace("\n", "")]
    return l, ms

def state(layout):
    ws = set()
    bs = set()
    r = None

    for i, line in enumerate(layout):
        for j, c in enumerate(line):
            if c == "#":
                ws.add((i, j))
            elif c == "O":
                bs.add((i, j))
            elif c == "@":
                r = (i, j)
    return ws, bs, r

def state2(layout):
    ws = set()
    bs = set()
    r = None

    for i, line in enumerate(layout):
        for j, c in enumerate(line):
            j *= 2
            if c == "#":
                ws.add((i, j))
                ws.add((i, j + 1))
            elif c == "O":
                bs.add((i, j))
            elif c == "@":
                r = (i, j)
    return ws, bs, r

def push(b, dir, bs, ws):
    npos = b[0] + dir[0], b[1] + dir[1]

    if npos in ws:
        return False
    if npos in bs:
        if not push(npos, dir, bs, ws):
            return False

    bs.remove(b)
    bs.add(npos)
    return True

def push2(b, dir, bs, ws):
    npos = b[0] + dir[0], b[1] + dir[1]
    lpos, rpos = (npos[0], npos[1] - 1), (npos[0], npos[1] + 1)

    if npos in ws or rpos in ws:
        return False
    if dir[0]:
        for pos in [npos, lpos, rpos]:
            if pos in bs:
                if not push2(pos, dir, bs, ws):
                    return False
    elif dir[1] == 1:
        if rpos in bs:
            if not push2(rpos, dir, bs, ws):
                return None
    elif dir[1] == -1:
        if lpos in bs:
            if push2(lpos, dir, bs, ws):
                return None

    bs.remove(b)
    bs.add(npos)
    return True

def s1(x, ms):
    ws, bs, r = state(x)

    for m in ms:
        npos = r[0] + m[0], r[1] + m[1]

        if npos in ws:
            continue
        if npos in bs:
            if not push(npos, m, bs, ws):
                continue
        r = npos
    return sum(100 * b[0] + b[1] for b in bs)

def s2(x, ms):
    ws, bs, r = state2(x)

    for m in ms:
        npos = r[0] + m[0], r[1] + m[1]

        if npos in ws:
            continue

        lpos = npos[0], npos[1] - 1
        if npos in bs or lpos in bs:
            bsc = bs.copy()
            bpos = npos if npos in bs else lpos
            if push2(bpos, m, bs, ws) is None:
                bs = bsc
                continue
        if npos not in bs and lpos not in bs:
            r = npos
    return sum(100 * b[0] + b[1] for b in bs)

with open(sys.argv[1]) as f:
    c = f.read()
    x, ms = parse(c)
    # print(ms)
    print(s1(x, ms))
    print(s2(x, ms))
