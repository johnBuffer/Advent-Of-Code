raw = [l.strip() for l in open('input')]
data = {(x, y): c for y, l in enumerate(raw) for x, c in enumerate(l)}
start = [(l.index('^'), y) for y, l in enumerate(raw) if '^' in l][0]

def predict(p, w):
    h, d = set(), (0, -1)
    while True:
        if (p, d) in h:
            return 1, 0
        h.add((p, d))
        nxt = (p[0] + d[0], p[1] + d[1])
        if not nxt in w:
            return 0, len(set(p for p, _ in h))
        elif w[nxt] == '#':
            d = (-d[1], d[0])
        else:
            p = nxt

print(predict(start, data)[1])
print(sum(predict(start, {pp: '#' if pp == p else cc for pp, cc in data.items()})[0] for p, c in data.items() if c != '#' and p != start))
