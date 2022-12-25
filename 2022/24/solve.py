d = [(x, y, c) for y, l in enumerate(open('data.txt')) for x, c in enumerate(l.strip())]
data, wall, X, Y = [x for x in d if x[2] in ['<', '>', '^', 'v']], {x[:2] for x in d if x[2] == '#'}, max(x[0] for x in d) + 1, max(x[1] for x in d) + 1

def update_blizzard(x, y, c): return (x + (c=='>') - (c=='<') - 1) % (X-2) + 1, (y + (c=='v') - (c=='^') - 1) % (Y-2) + 1, c
def update(world, time): return [update_blizzard(*b) for b in world], time + 1
def valid(x, y, w): return (-1<x<X) and (-1<y<Y) and (x, y) not in wall and not any((bx, by) == (x, y) for bx, by, _ in w)
def get_nxt(x, y, w): return [(a, b) for a, b in [(x, y), (x-1, y), (x+1, y), (x, y-1), (x, y+1)] if valid(a, b, w)]
def find_path(start, target, w):
    pos, (w, t) = [start], update(w, -1)
    while target not in pos: pos, (w, t) = set([(a, b) for p in pos for a, b in get_nxt(*p, w)]), update(w, t)
    return t, w

print(find_path((1, 0), (X-2, Y-1), data)[0])
time1, world = find_path((1, 0), (X-2, Y-1), data)
time2, world = find_path((X-2, Y-1), (1, 0), world)
time3, world = find_path((1, 0), (X-2, Y-1), world)
print(time1 + time2 + time3 + 2)