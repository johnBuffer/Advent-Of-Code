import re

def get(c, g):
    return [int(re.findall(f'.* (\d+) {c}.*', d)[0]) if c in d else 0 for d in g.split(';')]
games = [[get('red', l), get('green', l), get('blue', l)] for l in open('data.txt')]

print(sum((k + 1) * all(max(g[i]) <= 12 + i for i in range(3)) for k, g in enumerate(games)))
print(sum(max(g[0]) * max(g[1]) * max(g[2]) for g in games))
