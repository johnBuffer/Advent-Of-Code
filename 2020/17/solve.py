def offs(c, ranges, p=[], i=0):
    if i == len(c): yield tuple(p)
    else:
        for x in range(*ranges[i]): yield from offs(c, ranges, p + [c[i] + x], i+1)

def ns(p, c, data):
    a = sum(data.get(ps, 0) for ps in offs(list(p), [(-1, 2) for _ in p])) - c
    return 1 - c if (c and (a < 2 or a > 3)) or (c == 0 and a == 3) else c

def slv(g, d, c, i=1):
    return sum(g.values()) if i==c else slv({p: ns(p, g.get(p, 0), g) for p in offs([0]*len(d), [(-i, s+i) for s in d])}, d, c, i+1)

lines = [l.strip('\n') for l in open('input')]
dim = (len(lines[0]), len(lines), 1)
# Part 1
print(slv({(x, y, 0): v=='#' for y, l in enumerate(lines) for x, v in enumerate(l)}, dim, 7))
# Part 2
print(slv({(x, y, 0, 0): v=='#' for y, l in enumerate(lines) for x, v in enumerate(l)}, dim + tuple([1]), 7))

