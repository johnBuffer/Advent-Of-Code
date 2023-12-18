import math

data = [l.strip().split() for l in open('data.txt')]

def Area(corners): # Not mine
    n = len(corners)
    area = 0
    for i in range(n):
        j = (i + 1) % n
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) // 2
    return area

def solve(instr):
    current, vertices, contour = (0, 0), [(0, 0)], 0
    for d, c in instr:
        x, y = current
        if d == 'R':
            x += c
        elif d == 'L':
            x -= c
        elif d == 'U':
            y -= c
        elif d == 'D':
            y += c
        contour += c
        current = (x, y)
        vertices.append(current)
    return Area(vertices) + contour//2 + 1 # +1 because why not

print(solve([(d, int(c)) for (d, c, _) in data]))
print(solve([('RDLU'[int(h[-2])], int(h[2:-2], 16)) for (_, _, h) in data]))
