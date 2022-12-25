import re

def disjoint(x, y):
    return y[1] < x[0] or x[1] < y[0]

def fuse(x, y):
    a = min(x[0], y[0]) if x[0] <= y[1] else x[0]
    b = max(x[1], y[1]) if y[0] <= x[1] else x[1]
    return (a, b)

def insert(inter, other):
    res = []
    x, y, = inter
    for o in other:
        if disjoint(inter, o):
            res.append(o)
        else:
            x, y = fuse((x, y), o)
    return res + [(x, y)]

def width(x, y, a, b, pos):
    return 2 * (abs(x - a) + abs(y - b) - abs(pos - y)) + 1

def count(line_y, data):
    res = []
    for x, y, a, b in data:
        c = width(x, y, a, b, line_y)
        if c > 0:
            res = insert([x - c//2, x + c//2 + 1], res)
    return res

data = [[int(x) for x in re.findall(r'-*\d+', l)] for l in open('data.txt')]
no = set((x, y) for _, _, x, y in data) | set((x, y) for x, y, _, _ in data)

count_line = 0
for a, b in count(2000000, data):
    count_line += sum(((x, 2000000) not in no) for x in range(a, b))
print(count_line)

for y in range(4000001):
    if len(inters := count(y, data)) > 1:
        print(min(c[1] for c in inters) * 4000000 + y)
        break
