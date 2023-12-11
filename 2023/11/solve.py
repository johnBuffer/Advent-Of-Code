data = [l.strip() for l in open('data.txt')]
tdata = [''.join(r) for r in zip(*data)]
g = [(x, y) for y, l in enumerate(data) for x, c in enumerate(l) if c == '#']

def cost(c, e, transpose=False): # Cost of crossing a row or column
    return 1 if '#' in (tdata[c] if transpose else data[c]) else e

def dist(x1, x2, y1, y2, e): # Distance between 2 galaxies
    return sum(cost(x, e, True) for x in range(x1, x2)) + sum(cost(y, e) for y in range(y1, y2))

def get_dist(e): # Sum of pairs distance
    pairs = [((x, a), (y, b)) for i, (x, y) in enumerate(g) for k, (a, b) in enumerate(g) if k > i]
    return sum(dist(min(a), max(a), min(b), max(b), e) for a, b in pairs)

print(get_dist(2))
print(get_dist(1000000))