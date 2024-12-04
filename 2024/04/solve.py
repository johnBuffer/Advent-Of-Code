data = {(x, y): c for y, l in enumerate(open('input.txt')) for x, c in enumerate(l.strip())}

def cross(x, y): # Get substr in all directions
    return [''.join(data.get((x+i*dx, y+i*dy), '') for i in range(4)) for dx in [-1, 0, 1] for dy in [-1, 0, 1]]

def diag(x, y, v): # Extract a diagonal
    return ''.join(data.get((x+i, y+i*v), '') for i in range(-1, 2))

print(sum(sum(s == "XMAS" for s in cross(*p)) for p in data))
print(sum(all(d in ['MAS', 'SAM'] for d in [diag(*p, 1), diag(*p, -1)]) for p in data))
