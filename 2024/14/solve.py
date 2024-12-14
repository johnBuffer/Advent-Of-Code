import re

data = [[int(x) for x in re.findall(r'(-?\d+)', l)] for l in open('input')]
X, Y, n = 101, 103, 100

def step():
    for r in data: r[:2] = [(r[i]+r[2+i])%[X, Y][i] for i in (0, 1)]

def count(x1, y1, x2, y2):
    return sum(x1 <= a < x2 and y1 <= b < y2 for a, b, _, _ in data)

for _ in range(100):
    step()
a, b, c, d = count(0, 0, X//2, Y//2), count(X//2+1, 0, X, Y//2), count(0, Y//2+1, X//2, Y), count(X//2+1, Y//2+1, X, Y)
print(a*b*c*d)

while len(set((x, y) for x, y, _, _ in data)) < 500:
    n, _ = n + 1, step()
print(n)
