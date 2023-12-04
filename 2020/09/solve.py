def solve_1(d, s):
    for i, v in enumerate(d[s:]):
        if v not in [(m + n) for j, m in enumerate(d[i:i+s]) for n in d[i+j+1:i+s]]:
            return v

def solve_2(d, t):
    a, b, s = 0, 0, 0
    while s != t:
        a, b, s = a + (s > t), b + (s < t), s - d[a] * (s > t) + d[b] * (s < t)
    return min(data[a:b]) + max(data[a:b])

data = [int(l) for l in open('input')]
print(solve_1(data, 25))
print(solve_2(data, solve_1(data, 25)))
