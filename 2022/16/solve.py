from itertools import combinations as cb

data = [(a[6:8], int(a.split('=')[1]), [p[-2:] for p in b.split(', ')]) for a, b in [l.strip().split('; ') for l in open('data.txt')]]
graph = {v: [rate, out] for v, rate, out in data}
to_open = sum(v[0]>0 for v in graph.values())
g = {k: v[0] for k, v in graph.items()}

def distance(pos, end, explored, dist):
    if pos == end:
        return dist
    best = -1
    for o in [p for p in graph[pos][1] if p not in explored]:
        t = distance(end, o, explored | {pos}, dist + 1)
        if t != -1 and (t < best or best == -1):
            best = t
    return best

dists = {s: {e: distance(s, e, set(), 0) for e in graph if s != e and g[e] > 0} for s in graph if g[s] or s == 'AA'}

def find_pressure(pos, remaining, time, acc = 0, pressure = 0):
    if not remaining:
        return acc + pressure * time + g[pos] * (time-1)

    best = 0
    for o in remaining:
        t = dists[pos][o]
        pressure_at_arrival = acc + pressure * (t + 1) + g[pos] * t
        time_at_arrival = time - t - (g[pos] > 0)
        if time_at_arrival > 1:
            p = find_pressure(o, remaining - {o}, time_at_arrival, pressure_at_arrival, pressure + g[pos])
        else:
            p = acc + pressure * time + g[pos] * (time-1)
        best = max(best, p)
    
    return best


def brute_lol(d):
    return max(find_pressure('AA', set(c), 26) + find_pressure('AA', d - set(c), 26) for c in cb(d, len(d)//2))


print(find_pressure('AA', set(k for k,  v in g.items() if v), 30))
print(brute_lol(set(k for k, v in g.items() if v)))
