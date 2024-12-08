import math
data = {(x, y): c for y, l in enumerate(open('input')) for x, c in enumerate(l.strip())}

def get_normalized(x, y):
    d = math.gcd(x, y)
    return x // d, y // d

def is_antinode(x, y, s):
    return any(s.get((2*a-x, 2*b-y)) == c for (a, b), c in s.items() if (a, b) != (x, y))

def is_antinode_2(x, y, s):
    for (a, b), c in s.items():
        if (a, b) == (x, y):
            return 1
        vx, vy = get_normalized(a-x, b-y)
        if any(s.get((a+i*vx, b+i*vy)) == c for i in range(1, 50)):
            return 1
    return 0

print(sum(is_antinode(x, y, {p: c for p, c in data.items() if c != '.'}) for x, y in data))
print(sum(is_antinode_2(x, y, {p: c for p, c in data.items() if c != '.'}) for x, y in data))
