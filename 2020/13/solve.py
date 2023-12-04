import math

def solve_1(earliest, times):
    m = min([(t - earliest % t, t) for _, t in times], key = lambda t: t[0])
    return m[0] * m[1]

def solve_2(times):
    M = math.prod([t for _, t in times])
    YiMi = [M//t * pow(M//t, -1, t) for _, t in times]
    return sum([(t-i)*ym for ym, (i, t) in zip(YiMi, times)]) % M

raw_data = [l for l in open('input')]
earliest = int(raw_data[0])
times = [(i, int(t)) for i, t in enumerate(raw_data[1].split(',')) if t != 'x']

print(solve_1(earliest, times))
print(solve_2(times))
