import math

lines = [l[:-1] for l in open('input.txt')]
ops, lc, s = [p for p in lines[-1].split(' ') if p], len(lines) - 1, '.'

def solve(c, op): return sum(c) if op == '+' else math.prod(c)
def get_col(i): return ''.join(lines[k][i] for k in range(lc))
def is_num(num): return any(c != ' ' for c in num)

data = [[int(n) for n in p.split(' ') if n] for p in lines[:-1]]
print(sum(solve([data[k][i] for k in range(lc)], ops[i]) for i in range(len(data[0]))))
print(sum(solve(c, ops[i]) for i, c in enumerate([int(n) for n in c.split(s) if n] for c in s.join(get_col(i) for i in range(len(lines[0]))).split(' ' * lc))))