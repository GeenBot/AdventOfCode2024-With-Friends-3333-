from itertools import permutations
import sys

KEYPAD = {
    '7': (0, 0),
    '8': (1, 0),
    '9': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '1': (0, 2),
    '2': (1, 2),
    '3': (2, 2),
    '0': (1, 3),
    'A': (2, 3),
    '^': (1, 0),
    'a': (2, 0),
    '<': (0, 1),
    'v': (1, 1),
    '>': (2, 1)
}

DIRS = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0)
}

def seq_to_moves(start, end, avoid):
    dy, dx = end[0] - start[0], end[1] - start[1]
    moves = []

    if dx < 0:
        moves.extend(['^'] * abs(dx))
    else:
        moves.extend(['v'] * dx)
    if dy < 0:
        moves.extend(['<'] * abs(dy))
    else:
        moves.extend(['>'] * dy)

    seqs = []
    for perm in set(permutations(moves)):
        ps = [start]
        valid = True
        for move in perm:
            npos = ps[-1][0] + DIRS[move][0], ps[-1][1] + DIRS[move][1]
            if npos == avoid:
                valid = False
                break
            ps.append(npos)
        if valid:
            seqs.append(''.join(perm) + 'a')
    return seqs

memo = {}
def dp(seq, limit, depth = 0):
    key = (seq, depth, limit)
    if key in memo:
        return memo[key]

    avoid = (0, 3) if depth == 0 else (0, 0)
    current = KEYPAD['A'] if depth == 0 else KEYPAD['a']

    total = 0
    for c in seq:
        npos = KEYPAD[c]
        moves = seq_to_moves(current, npos, avoid)

        if depth >= limit:
            total += len(min(moves, key=len))
        else:
            minm = float('inf')
            for move in moves:
                length = dp(move, limit, depth + 1)
                minm = min(minm, length)
            total += minm
        current = npos

    memo[key] = total
    return total

def s1(c):
    codes = [line.strip() for line in c.splitlines() if line.strip()]
    total = 0

    for code in codes:
        length = dp(code, 2)
        numeric = int(''.join(c for c in code if c.isdigit()))
        total += length * numeric

    return total

def s2(c):
    codes = [line.strip() for line in c.splitlines() if line.strip()]
    total = 0

    for code in codes:
        length = dp(code, 25)
        numeric = int(''.join(c for c in code if c.isdigit()))
        total += length * numeric

    return total

with open(sys.argv[1]) as f:
    c = f.read()
    print(s1(c))
    print(s2(c))
