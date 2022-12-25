data = [[tuple(int(x) for x in p.split(','))for p in l.strip().split(' -> ')] for l in open('data.txt')]

def adv(x, y): return tuple(a + (1 if b > a else -1 if b < a else 0) for a, b in zip(x, y))
def trace(p, d, s = set()): return trace(d[0], d[1:], s | {p}) if d and p == d[0] else trace(adv(p, d[0]), d, s | {p}) if d else s
def get_free(x, y): return [(a, b) for a, b  in [(x, y+1), (x-1, y+1), (x+1, y+1), (x, y)] if (a, b) not in res][0]
def sand(p, last=(0, 0)): return sand(get_free(*p), p) if p[1] != Y and last != p else res | {p}

res = set(c for t in data for c in trace(t[0], t[1:]))
base_count, Y, S = len(res), max(y for _, y in res) + 1, (500, 0)

while Y not in [y for _, y in res]: res = sand(S)
print(len(res) - base_count - 1)
while S not in res: res = sand(S)
print(len(res) - base_count)