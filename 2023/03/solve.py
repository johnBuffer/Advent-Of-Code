from collections import defaultdict
data = {(x, y): c for y, l in enumerate(open('data.txt')) for x, c in enumerate(l.strip() + '.')}

def get_symbol(x, y):
    return [(s, a, b) for a in [x-1, x, x+1] for b in [y-1, y, y+1] if (s := data.get((a, b), '.')) not in '.0123456789']

current_symbol, n, symbols = None, 0, defaultdict(list)
for p in [(a, b) for b in range(140) for a in range(141)]:
    num = data[p].isdigit()
    if current_symbol and not num: symbols[current_symbol[0]] += [n]
    current_symbol = get_symbol(*p) or current_symbol if num else None
    n = 10 * n + int(data[p]) if num else 0

print(sum(sum(v) for v in symbols.values()))
print(sum(v[0] * v[1] for k, v in symbols.items() if k[0] == '*' and len(v) == 2))