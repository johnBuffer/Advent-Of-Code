def parse_line(line):
    cmd, arg = line.split(' ')
    return (cmd != 'jmp') + (cmd == 'jmp') * int(arg), (cmd == 'acc') * int(arg), cmd, int(arg)

def solve_1(pgrm, executed, discard=False, counter=0, acc=0):
    while len(pgrm) > counter > -1 and not executed[counter] and not discard:
        executed[counter], (counter, acc) = True, map(sum, zip([counter, acc], pgrm[counter][:-2]))
    return acc, counter == len(pgrm)

def solve_2(p, i=0, done=False, acc=0):
    while not done:
        _, _, cmd, arg = p[i]
        idx = ['jmp', 'nop', 'acc'].index(cmd)
        (acc, done), i = solve_1(p[0:i] + [(idx * arg - idx + 1, 0, '', arg)] + p[i+1:], [False]*len(p), idx == 2), i+1
    return acc

program = [parse_line(l)  for l in open('input', 'r')]
print(solve_1(program, [False] * len(program))[0])
print(solve_2(program))
