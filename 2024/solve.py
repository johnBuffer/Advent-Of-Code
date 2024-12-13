import re
INF = 1000000000

def parse():
    raw, data = open('input').read().split('\n\n'), []
    for l in raw:
        data.append([[int(x) for x in re.findall(r'(\d+)', p)] for p in l.split('\n')])
    return data

data = parse()


def cost(m, cache, x=0, y=0, a=0, b=0):
    key = (x, y, a, b)
    if key in cache:
        return cache[key]
    
    (xA, yA), (xB, yB), (tX, tY) = m
    if (x, y) == (tX, tY):
        cache[key] = 3 * a + b
        return cache[key]
    
    if x > tX or y > tY:
        cache[key] = INF
        return cache[key]
    
    pressA = cost(m, cache, x+xA, y+yA, a+1, b)
    pressB = cost(m, cache, x+xB, y+yB, a, b+1)
    cache[key] = min(pressA, pressB)
    return cache[key]


s = 0
for m in data:
    cache = {}
    c = cost(m, cache)
    s += c if c != INF else 0
print(s)
