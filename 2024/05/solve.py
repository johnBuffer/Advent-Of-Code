ri, ui = open('input.txt').read().split('\n\n')
rules, updates = [[int(x) for x in l.split('|')] for l in ri.split('\n')], [tuple(map(int, l.split(','))) for l in ui.split('\n')]
cond, cache = {(n, u): {a for a, b in rules if b == n and a in u} for u in updates for n in u}, {}

def rank(n, u):
    return cache.get(n) or cache.update({n: max([rank((x, u), u) for x in cond[n]] + [0]) + 1}) or cache[n]

def sort(u):
    return tuple(sorted(u, key=lambda n: rank((n, u), u)))

print(sum(u[len(u)//2] for u in updates if u == sort(u)))
print(sum(sort(u)[len(u)//2] for u in updates if u != sort(u)))