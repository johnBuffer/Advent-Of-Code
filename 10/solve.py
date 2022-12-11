pr, data, s = print, [0 if p in ['addx', 'noop'] else int(p) for l in open('data.txt') for p in l.strip().split()], (1, 0, 0)
def xs(i, r, c=1): return xs(i[1:], r + [(r[-1][0] + i[0], c+1, c%40)], c+1) if i else r

pr(sum(x * c * (m == 19) for x, c, m in xs(data, [s])))
pr(''.join(('#' if (x-1) <= m <= (x+1) else ' ') + '\n' * (m == 39) for x, _, m in xs(data, [s])))