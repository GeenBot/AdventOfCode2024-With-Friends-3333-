import sys

def do(inputs, gates):
    while True:
        c = False

        for g in gates:
            ins, out = g.split(" -> ")
            parts = ins.split()

            if out in inputs:
                continue

            if len(parts) == 1:
                if parts[0] in inputs:
                    inputs[out] = inputs[parts[0]]
                    c = True
            elif len(parts) == 3:
                w1, op, w2 = parts

                if w1 not in inputs or w2 not in inputs:
                    continue

                v1, v2 = inputs[w1], inputs[w2]

                if op == "AND":
                    inputs[out] = v1 & v2
                elif op == "OR":
                    inputs[out] = v1 | v2
                elif op == "XOR":
                    inputs[out] = v1 ^ v2
                c = True
        if not c:
            break

    return inputs

def parse(c):
    ins, gates = c.strip().split("\n\n")
    inputs = {}

    for line in ins.split("\n"):
        wire, v = line.split(": ")
        inputs[wire] = int(v)

    return inputs, gates.split("\n")

def bin(wires):
    zs = []
    for k in wires.keys():
        if k.startswith("z"):
            num = int(k[1:])
            zs.append((num, k))
    binary = ''.join(str(wires[wire]) for _, wire in reversed(sorted(zs)))

    return int(binary, 2)

def find_gate(a, b, op, gates):
    for gate in gates.split("\n"):
        if f"{a} {op} {b}" in gate or f"{b} {op} {a}" in gate:
            return gate.split(" -> ")[1]
    return None

def s1(c):
    inputs, gates = parse(c)
    return bin(do(inputs, gates))

def s2(c):
    inputs, gates = c.strip().split("\n\n")
    swapped = []
    c0 = None

    for i in range(45):
        n = f"{i:02}"
        m1 = find_gate(f"x{n}", f"y{n}", "XOR", gates)
        n1 = find_gate(f"x{n}", f"y{n}", "AND", gates)

        if c0 is not None: # if we have a carry from previous bit
            r1 = find_gate(c0, m1, "AND", gates)
            if not r1: # AND between carry and current sum should exist
                m1, n1 = n1, m1
                swapped.extend([m1, n1])
                r1 = find_gate(c0, m1, "AND", gates)
            z1 = find_gate(c0, m1, "XOR", gates)

            if m1 and m1.startswith("z"): # m1 is an intermediate sum, shouldnt be z
                m1, z1 = z1, m1
                swapped.extend([m1, z1])

            if n1 and n1.startswith("z"): # n1 is a half added carry, shouldnt be z
                n1, z1 = z1, n1
                swapped.extend([n1, z1])

            if r1 and r1.startswith("z"): # r1 is a carry gen, shouldnt be z
                r1, z1 = z1, r1
                swapped.extend([r1, z1])

            c1 = find_gate(r1, n1, "OR", gates)

            if c1 and c1.startswith("z") and c1 != "z45": # c1 is carry out, shouldnt be z (except z45)
                c1, z1 = z1, c1
                swapped.extend([c1, z1])
        c0 = c1 if c0 else n1
    return ','.join(sorted(list(set(swapped))))

with open(sys.argv[1]) as f:
    c = f.read()
    print(s1(c))
    print(s2(c))
