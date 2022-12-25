def in_sight(row, col, grid, dr, dc, md):
    h, w, r, c, d, l = len(grid), len(grid[0]), row + dr, col + dc, 1, 2
    while h > r > -1 and w > c > -1 and d <= md and l > 1:
        r, c, d, l = r + dr, c + dc, d + 1, grid[r][c]
    return l%2

def occupied(row, col, grid, md):
    return sum([in_sight(row, col, grid, i, j, md) for i in [-1, 0, 1] for j in [-1, 0, 1] if i or j])

def next_state(cur, occ, ms):
    return 1 - cur if (not cur) * (not occ) + (cur%2) * (occ > ms) else cur

def simulate(g, md, ms):
    return [[next_state(cl, occupied(r, c, g, md), ms) for c, cl in enumerate(rw)] for r, rw in enumerate(g)]

def solve(current, last, md, ms):
    return sum(r.count(1) for r in current) if current == last else solve(simulate(current, md, ms), current, md, ms)

data = [[2 * (c == '.') for c in l.strip('\n')] for l in open('input')]
print(solve(data, None, 1, 3))
print(solve(data, None, max(len(data), len(data[0])), 4))
