data = [list(l.strip()) for l in open('data.txt')]

def get_min(nodes): return min([(c, d) for c, (_, d, v) in nodes.items() if d != -1 and not v] + [(None, 10000)], key=lambda x: x[1])[0]
def dist(ch, cd, _, nxt, check): nxt[1] = cd + 1 if check(nxt[0], ch) and not nxt[2] and (cd + 1 < nxt[1] or nxt[1] == -1) else nxt[1]
def calc(nodes, cx, cy, ox, oy, check): return dist(*nodes[(cx, cy)], nodes[(cx+ox, cy+oy)], check) if (cx+ox, cy+oy) in nodes else None
def calc_dists(cur, check):
    nodes = {(x, y): [ord(c.replace('S', 'a').replace('E', 'z')), -1 * (cur!=(x, y)), False] for y, l in enumerate(data) for x, c in enumerate(l)}
    while cur is not None: _, nodes[cur][2], cur = [calc(nodes, *cur, *nc, check) for nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]], True, get_min(nodes)
    return nodes

target, start = [(l.index('E'), y) for y, l in enumerate(data) if 'E' in l][0], [(l.index('S'), y) for y, l in enumerate(data) if 'S' in l][0]
print(calc_dists(start, lambda x, y: x < y + 2)[target][1])
print(min(d for (h, d, _) in calc_dists(target, lambda x, y: x > y - 2).values() if h == ord('a') and d != -1))