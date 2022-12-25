from collections import deque 

data = set(tuple(int(x) for x in l.strip().split(',')) for l in open('data.txt'))
start = tuple(min(c[i]-1 for c in data) for i in range(3))
end = tuple(max(c[i]+1 for c in data) for i in range(3))

def is_valid(p):
    return all(start[k] <= p[k] <= end[k] for k in range(3))

def get_around(p):
    around = []
    for i in range(3):
        for d in [-1, 1]:
            around.append(tuple(p[k] + d * (k==i) for k in range(3)))
    return set(c for c in around if is_valid(c))

def surface():
    res, done, todo = 0, set(), deque([start])
    while todo:
        current = todo.popleft()
        done.add(current)
        for check in get_around(current):
            if check in data:
                res += 1
            elif check not in todo and check not in done:
                todo.append(check)
    return res

print(6 * len(data) - sum(sum(c in data for c in get_around(p)) for p in data))
print(surface())