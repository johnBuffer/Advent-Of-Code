data = [0 if p in ['addx', 'noop'] else int(p) for l in open('data.txt') for p in l.strip().split()]
def xs(i, r, c=1): return xs(i[1:], r + [(r[-1][0] + i[0], c, c%40)], c + 1) if i else r

print(sum(x * (c + 1) for x, c, m in xs(data, [(1, 0, 0)]) if m == 19))
print(''.join(('#' if (x-1) <= m <= (x + 1) else ' ') + '\n' * (m == 39) for x, c, m in xs(data, [(1, 0, 0)])))