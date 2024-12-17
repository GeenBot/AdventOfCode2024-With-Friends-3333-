import sys

def parse(c):
    lines = c.strip().split('\n')

    a = int(lines[0].split(': ')[1])
    b = int(lines[1].split(': ')[1])
    c = int(lines[2].split(': ')[1])

    part = lines[4].split(': ')[1]
    program = [int(x) for x in part.split(',')]

    return program, a, b, c

def run_program(program, reg_a, reg_b=0, reg_c=0):
    rs = {'a': reg_a, 'b': reg_b, 'c': reg_c}
    outputs = []
    ip = 0

    def combo(operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return rs['a']
        elif operand == 5:
            return rs['b']
        elif operand == 6:
            return rs['c']

    while ip < len(program) - 1:
        opcode = program[ip]
        operand = program[ip + 1]

        if opcode == 0:
            power = combo(operand)
            rs['a'] = rs['a'] // (2 ** power)
            ip += 2

        elif opcode == 1:
            rs['b'] ^= operand
            ip += 2

        elif opcode == 2:
            rs['b'] = combo(operand) % 8
            ip += 2

        elif opcode == 3:
            if rs['a'] != 0:
                ip = operand
            else:
                ip += 2

        elif opcode == 4:
            rs['b'] ^= rs['c']
            ip += 2

        elif opcode == 5:
            outputs.append(combo(operand) % 8)
            ip += 2

        elif opcode == 6:
            power = combo(operand)
            rs['b'] = rs['a'] // (2 ** power)
            ip += 2

        elif opcode == 7:
            power = combo(operand)
            rs['c'] = rs['a'] // (2 ** power)
            ip += 2
    return outputs

def s1(program):
    return ','.join(str(x) for x in run_program(program, a, b, c))

def s2(program):
    valid = [0]

    for l in range(1, len(program) + 1):
        out = []
        for num in valid:
            for offset in range(2 ** 3):
                a = (2 ** 3) * num + offset
                if run_program(program, a) == program[-l:]:
                    out.append(a)
        valid = out

    return min(valid)

with open(sys.argv[1]) as f:
    program, a, b, c = parse(f.read())
    print(s1(program))
    print(s2(program))
