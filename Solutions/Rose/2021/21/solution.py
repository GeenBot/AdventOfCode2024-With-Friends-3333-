from functools import cache

def sol(p1, p2):
    pos1, pos2 = p1, p2
    score1 = score2 = 0

    val = 1
    rolls = 0

    while True:
        move = 0

        for _ in range(3):
            move += val
            val = val % 100 + 1
            rolls += 1

        pos1 = ((pos1 + move - 1) % 10) + 1
        score1 += pos1

        if score1 >= 1000:
            return score2 * rolls

        move = 0

        for _ in range(3):
            move += val
            val = val % 100 + 1
            rolls += 1

        pos2 = ((pos2 + move - 1) % 10) + 1
        score2 += pos2

        if score2 >= 1000:
            return score1 * rolls

@cache
def dp(pos1, pos2, score1, score2):
    if score2 >= 21:
        return (0, 1)
    if score1 >= 21:
        return (1, 0)

    wins1 = 0
    wins2 = 0

    for d1 in range(1, 4):
        for d2 in range(1, 4):
            for d3 in range(1, 4):
                sum = d1 + d2 + d3
                npos1 = ((pos1 + sum - 1) % 10) + 1
                npos2 = score1 + npos1
                sub2, sub1 = dp(pos2, npos1,score2, npos2)

                wins1 += sub1
                wins2 += sub2

    return (wins1, wins2)

def sol2(p1, p2):
    return max(dp(p1, p2, 0, 0))

print(sol(9, 10))
print(sol2(9, 10))
