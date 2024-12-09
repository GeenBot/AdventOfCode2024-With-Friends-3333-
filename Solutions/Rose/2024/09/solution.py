import sys

def s1(ns):
    bls = []
    id = 0

    for i in range(0, len(ns), 2):
        n = ns[i]
        for j in range(n):
            bls.append(id)
        id += 1
        if i + 1 < len(ns):
            bls.extend([-1] * ns[i + 1])

    while True:
        spos = -1
        for i in range(len(bls)):
            if bls[i] == -1:
                spos = i
                break
        if spos == -1: break

        fpos = -1
        for i in range(len(bls) - 1, spos, -1):
            if bls[i] != -1:
                fpos = i
                break
        if fpos == -1: break

        bls[spos] = bls[fpos]
        bls[fpos] = -1

    return sum(pos * id for pos, id in enumerate(bls) if id != -1)

def s2(ns):
    szs = {}
    bls = []
    id = 0

    for i in range(0, len(ns), 2):
        n = ns[i]
        szs[id] = n
        for j in range(n):
            bls.append(id)
        id += 1
        if i + 1 < len(ns):
            bls.extend([-1] * ns[i + 1])

    for id in range(max(szs.keys()), -1, -1):
        if id not in szs:
            continue

        sz = szs[id]
        start = -1
        for i in range(len(bls)):
            if bls[i] == id:
                start = i
                break

        bpos = -1
        sc = 0
        for i in range(len(bls)):
            if bls[i] == -1:
                sc += 1
                if sc >= sz:
                    bpos = i - sz + 1
                    break
            else:
                sc = 0

        if bpos != -1 and bpos < start:
            for i in range(start, start + sz):
                bls[i] = -1
            for i in range(bpos, bpos + sz):
                bls[i] = id

    return sum(pos * id for pos, id in enumerate(bls) if id != -1)

with open(sys.argv[1]) as f:
    data = f.read().strip()
    ns = [int(x) for x in data]
    print(s1(ns))
    print(s2(ns))
