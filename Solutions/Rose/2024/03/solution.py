import sys
import re

def s1(contents):
    pat = r"mul\((\d+),(\d+)\)"
    mat = re.findall(pat, contents)
    res = sum(int(x) * int(y) for x, y in mat)

    return res

def s2(contents):
    pat = r"mul\((\d+),(\d+)\)"
    do = r"do\(\)"
    dont = r"don't\(\)"

    mul = True
    s = 0
    i = 0

    while i < len(contents):
        if re.match(do, contents[i:]):
            mul = True
            i += len("do()")
        elif re.match(dont, contents[i:]):
            mul = False
            i += len("don't()")
        else:
            mat = re.match(pat, contents[i:])
            if mat:
                x, y = map(int, mat.groups())
                if mul:
                    s += x * y
                i += len(mat.group(0))
            else:
                i += 1

    return s

with open(sys.argv[1]) as f:
    d = f.read()
    print(s1(d))
    print(s2(d))
