data = [[c for c in l.strip()] for l in open('input.txt')]
split, beam, hist = 0, data[0], {}

def valid(i): return 0 <= i < len(data[0])

for l in data[1:]:
    for i, c in enumerate(l):
        if beam[i] == 'S':
            if c == '^':
                split += 1
                for k in [(i - 1), (i + 1)]:
                    if valid(k): l[k] = 'S'
            else:
                l[i] = 'S'
    beam = l
print(split)

def count(i, lines, li):
    k = (li, i)
    if k not in hist:
        if not lines:
            hist[k] = 1
        else:
            h, *t = lines
            hist[k] = (count(i-1, t, li+1) + count(i+1, t, li+1) if h[i] == '^' else count(i, t, li+1)) if valid(i) else 0
    return hist[k]
print(count(data[0].index('S'), data[1:], 0))
