import math

data = [[int(x) for x in l.strip().split(',')] + [i] for i, l in enumerate(open('input.txt'))]

def dist(a, b):
    return math.sqrt(sum((x - y)**2 for x, y in zip(a[:3], b[:3])))

def create_pairs():
    return sorted([(i, k) for i in range(len(data)) for k in range(i + 1, len(data))], key=lambda a: dist(data[a[0]], data[a[1]]))

def already_connected(a, b):
    return data[a][3] == data[b][3]

def connect(a, b):
    return False if already_connected(a, b) else merge(data[a][3], data[b][3]) or True

circuits, pairs = {i: [i] for i in range(len(data))}, create_pairs()

def merge(c1, c2):
    circuits[c1] += circuits[c2]
    for i in circuits[c2]:
        data[i][3] = c1
    circuits.pop(c2, None)

for i in range(1000):
    connect(*pairs[i])
print(math.prod(len(x) for x in sorted(circuits.values(), key=lambda x: len(x), reverse=True)[:3]))

i = res = 0
while len(circuits) > 1:
    a, b = pairs[i]
    if connect(a, b):
        res = data[a][0] * data[b][0]
    i += 1
print(res)