world = {(x, y): c for y, l in enumerate(open('input')) for x, c in enumerate(l.strip())}

def connected(x, y):
    return [(x+dx, y+dy) for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]]

def split():
    res, to_visit = [], set(world.keys())
    while len(to_visit):
        region, to_visit_region = [], [list(to_visit)[0]]
        kind = world[to_visit_region[0]]
        while len(to_visit_region):
            p = to_visit_region.pop()
            region.append(p)
            to_visit.remove(p)
            for np in connected(*p):
                if world.get(np) == kind and np not in to_visit_region and np not in region:
                    to_visit_region.append(np)
        res.append(region)
    return res

def getCellPerim(p, c):
    return sum(world.get(np) != c for np in connected(*p))

def perimeter(r, c):
    return sum(getCellPerim(p, c) for p in r)

def extractSide(nrm, l):
    dir, lvl, res = bool(nrm[0]), bool(nrm[1]), 0
    while l:
        p0 = l.pop()
        a, b, found = p0[dir], p0[dir], True
        while found:
            found = False
            for p1 in l:
                if p1[lvl] == p0[lvl] and p1[dir] in (a-1, b+1):
                    l.remove(p1)
                    a, b, found = min(a, p1[dir]), max(b, p1[dir]), True
            if not found:
                res += 1
    return res

def countSides(r):
    sides = {s: [] for s in [(0, -1), (1, 0), (0, 1), (-1, 0)]}
    for x, y in r:
        for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
            nx, ny = x+dx, y+dy
            if (nx, ny) not in r: # We are on the perimeter
                sides[(dx, dy)].append((x, y)) # Add the cell in the corresponding side list

    return sum(extractSide(*i) for i in sides.items())

print(sum(len(r) * perimeter(r, world[r[0]]) for r in split()))
print(sum(len(r) * countSides(r) for r in split()))
