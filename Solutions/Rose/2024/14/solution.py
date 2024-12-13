import sys

def s1(c):
    pass

def s2(c):
    pass

with open(sys.argv[1]) as f:
    c = f.read()
    print(s1(c))
    print(s2(c))
