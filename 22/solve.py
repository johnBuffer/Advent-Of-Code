data = open('data.txt').read().split('\n')
world = data[:-2]
moves = [int(x) for l in data[-1].split('R') for x in l.split('L')]
dirs  = [c for c in data[-1] if c in ['R', 'L']] + [' ']

# Very not generic
connections = [
    (range(150, 151), range(  0,  50), ( 1,  0), lambda x, y: (99, 100 + 49 - y)  , (-1,  0)), # 0
    (range(100, 150), range( -1,   0), ( 0, -1), lambda x, y: (x - 100, 199)      , ( 0, -1)), # 1
    (range(100, 150), range( 50,  51), ( 0,  1), lambda x, y: (99, 50 + x - 100)  , (-1,  0)), # 2
    (range( 50, 100), range( -1,   0), ( 0, -1), lambda x, y: (0, 150 + x - 50)   , ( 1,  0)), # 3
    (range( 49,  50), range(  0,  50), (-1,  0), lambda x, y: (0, 100 + 49 - y)   , ( 1,  0)), # 4
    (range( 49,  50), range( 50, 100), (-1,  0), lambda x, y: (y - 50, 100)       , ( 0,  1)), # 5
    (range(100, 101), range( 50, 100), ( 1,  0), lambda x, y: (100 + y - 50, 49)  , ( 0, -1)), # 6
    (range(100, 101), range(100, 150), ( 1,  0), lambda x, y: (149, 149 - y)      , (-1,  0)), # 7
    (range( 50, 100), range(150, 151), ( 0,  1), lambda x, y: ( 49, 150 + x - 50) , (-1,  0)), # 8
    (range( 50,  51), range(150, 200), ( 1,  0), lambda x, y: (50 + y - 150, 149) , ( 0, -1)), # 9
    (range(  0,  50), range(200, 201), ( 0,  1), lambda x, y: (100 + x, 0)        , ( 0,  1)), # 10
    (range( -1,   0), range(150, 200), (-1,  0), lambda x, y: (50 + y - 150, 0)   , ( 0,  1)), # 11
    (range( -1,   0), range(100, 150), (-1,  0), lambda x, y: (50, 149 - y)       , ( 1,  0)), # 12
    (range(  0,  50), range( 99, 100), ( 0, -1), lambda x, y: (50, 50 + x)        , ( 1,  0)), # 13
]

def adv(p, v): return (p[0] + v[0], p[1] + v[1])

def need_wrap(x, y): return any(x in rx and y in ry for rx, ry, _, _, _ in connections)

def wrap_cube(x, y, v):
    for rx, ry, vc, transform, nv in connections:
        if (x in rx) and (y in ry) and (v == vc):
            nx, ny = transform(x, y)
            return ((x, y), v) if world[ny][nx] == '#' else ((nx, ny), nv)

def walk(p, v, dist):
    for _ in range(dist):
        x, y = adv(p, v)
        if need_wrap(x, y):
            np, nv = wrap_cube(x, y, v)
            if np == (x, y): break
            else: p, v = np, nv
        elif world[y][x] == '.': p = (x, y)
        else: break
    return p, v

def get_start():
    return (world[0].find('.'), 0)

def rotate(v, d):
    if d == 'R':
        return (-v[1], v[0])
    elif d == 'L':
        return (v[1], -v[0])
    return v

def follow():
    p = get_start()
    v = (1, 0)
    for n, r in zip(moves, dirs):
        p, v = walk(p, v, n)
        v = rotate(v, r)
    return 1000 * (p[1] + 1) + 4 * (p[0] + 1) + [(1, 0), (0, 1), (-1, 0), (0, -1)].index(v)

# osef part 1
print(follow())