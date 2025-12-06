import math
lines = [l[:-1] for l in open('input.txt')]
ops, lc = [p for p in lines[-1].split(' ') if p], len(lines) - 1
pos = [i for i, c in enumerate(lines[-1]) if c != ' '] + [len(lines[-1]) + 2]
groups = [[lines[i][a:b-1] for i in range(lc)] for a, b in zip(pos, pos[1:])]

def solve(g, op): return (sum if op == '+' else math.prod)(int(n) for n in g)

print(sum(solve(*o) for o in zip(groups, ops)))
print(sum(solve([''.join(c) for c in zip(*g)], o) for g, o in zip(groups, ops)))