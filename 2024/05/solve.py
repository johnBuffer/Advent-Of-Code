ri, ui = open('input.txt').read().split('\n\n')
rules, updates = [[int(x) for x in l.split('|')] for l in ri.split('\n')], [tuple(map(int, l.split(','))) for l in ui.split('\n')]
cond, cache = {n: {a for a, b in rules if b == n} for n in set(x for u in updates for x in u)}, {}

def rank(n, u):
    return cache.get((n, u)) or cache.update({(n, u): max([rank(x, u) for x in cond[n] if x in u] + [-1]) + 1}) or cache[(n, u)]

def sort(u):
    return tuple(sorted(u, key=lambda n: rank(n, u)))

print(sum(u[len(u)//2] for u in updates if u == sort(u)))
print(sum(sort(u)[len(u)//2] for u in updates if u != sort(u)))