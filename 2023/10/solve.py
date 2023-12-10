pipes = {'L': [( 0, -1), ( 1, 0)],
         '7': [(-1,  0), ( 0, 1)],
         '|': [( 0, -1), ( 0, 1)],
         '-': [(-1,  0), ( 1, 0)],
         'J': [( 0, -1), (-1, 0)],
         'F': [( 1,  0), ( 0, 1)]}

raw = [l.strip() for l in open('data.txt')]
data = {(x, y): c for y, l in enumerate(open('data.txt')) for x, c in enumerate(l.strip())}
graph = {}
for (x, y), c in data.items():
    if c == 'S':
        start = (x, y)
    if c in pipes:
        graph[(x, y)] = [((x + dx), (y + dy)) for dx, dy in pipes[c]]

start = (85, 79)
data[start] = 'J'
visited = set([start])
nxt, prv = (84, 79), start
while nxt not in visited or prv not in visited:
    cur = nxt if (nxt not in visited) else prv
    visited.add(cur)
    nxt, prv = graph[cur]
print(len(visited)//2)

res = 0
for x in range(len(raw[0])):
    is_in = False
    for y in range(len(raw)):
        if (x, y) in visited:
            if data[(x, y)] in 'F-L':
                is_in = not is_in
        else:
            res += is_in
print(res)


