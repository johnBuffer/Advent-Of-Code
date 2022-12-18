data = set(tuple(int(x) for x in l.strip().split(',')) for l in open('data.txt'))
O, M = tuple(min(c[i]-1 for c in data) for i in range(3)),tuple(max(c[i]+2 for c in data) for i in range(3))

def is_valid(p): return all(O[k] <= p[k] <= M[k] for k in range(3))
def get_around(p): return set(c for c in [tuple(p[k] + d * (k==i) for k in range(3)) for i in range(3) for d in [-1, 1]] if is_valid(c))
def explore(around, todo, done, res): return res + len(around & data), todo[1:] + list(around - data - done - set(todo)), done | {todo[0]}
def surface():
    res, done, todo = 0, set(), [O]
    while todo: res, todo, done = explore(get_around(todo[0]), todo, done, res) 
    return res

print(6 * len(data) - sum(sum(c in data for c in get_around(p)) for p in data))
print(surface())