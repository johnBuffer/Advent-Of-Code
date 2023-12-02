import re

def extract(color, game):
    return [int(re.findall(f'.* (\d+) {color}.*', d)[0]) if color in d else 0 for d in game.split(';')]
games = [[extract(c, l) for c in ['red', 'green', 'blue']] for l in open('data.txt')]

print(sum((k + 1) * all(max(g[i]) <= 12 + i for i in range(3)) for k, g in enumerate(games)))
print(sum(max(g[0]) * max(g[1]) * max(g[2]) for g in games))