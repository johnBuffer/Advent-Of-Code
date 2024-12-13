import re
from scipy.optimize import linprog

def parse():
    raw, data = open('input').read().split('\n\n'), []
    for l in raw:
        data.append([[int(x) for x in re.findall(r'(\d+)', p)] for p in l.split('\n')])
    return data

def valid(res):
    return res is not None and all(x%1 < 0.001 or x%1 > 0.999 for x in res)

def cost(m, o):
    a, b = list(zip(m[0], m[1])), [x + o for x in m[2]]
    if valid(res := linprog([3, 1], A_eq=a, b_eq=b).x):
        return 3 * round(res[0]) + round(res[1])
    return 0

print(sum(cost(m, 0) for m in parse()))
print(sum(cost(m, 10000000000000) for m in parse()))
