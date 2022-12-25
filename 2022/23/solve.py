data = set([(x, y) for y, l in enumerate(open('data.txt')) for x, c in enumerate(l) if c == '#'])
check_order = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def increase(pos, orig, d): d[pos] = d[pos] + [orig] if pos in d else [orig]
def count_free(p): return ((max(x for x, _ in p)+1)-min(x for x, _ in p)) * ((max(y for _, y in p)+1)-min(y for _, y in p)) - len(p)

def round(start, checks, pg):
    for x, y in start:
        found = False
        if any((x + a, y + b) in start for a in range(-1, 2) for b in range(-1, 2) if a or b):
            for cx, cy in checks:
                if all(p not in start for p in [(x+cx+(d*(cy!=0)), y+cy+(d*(cx!=0))) for d in [-1, 0, 1]]):
                    increase((x + cx, y + cy), (x, y), pg)
                    found = True
                    break
        if not found:
            increase((x, y), (x, y), pg)
    return set([x for k, v in pg.items() for x in ([k] if (len(v) == 1) else v)])

pos, check = set([p for p in data]), [c for c in check_order]
for _ in range(10): pos, check = round(pos, check, {}), check[1:] + check[:1]
print(count_free(pos))

pos, check, i = set([p for p in data]), [c for c in check_order], 1
while True:
    next_pos = round(pos, check, {})
    if next_pos == pos: break
    pos, check, i = next_pos, check[1:] + check[:1], i + 1
print(i)