raw = [l.strip() for l in open('data.txt')]
data = [(x, y, c) for y, l in enumerate(raw) for x, c in enumerate(l) if c in ['<', '>', '^', 'v']]
wall = {(x, y) for y, l in enumerate(raw) for x, c in enumerate(l) if c == '#'}
X, Y = len(raw[0]), len(raw)

def update_blizzard(x, y, c):
    next_x = (x + (c=='>') - (c=='<') - 1) % (X-2) + 1
    next_y = (y + (c=='v') - (c=='^') - 1) % (Y-2) + 1
    return (next_x, next_y, c)

def update(world):
    return [update_blizzard(*b) for b in world]

def valid(x, y, world): 
    in_world = (-1 < x < X) and (-1 < y < Y)
    no_wall  = (x, y) not in wall
    no_bliz  = not any((bx, by) == (x, y) for bx, by, _ in world)
    return in_world and no_wall and no_bliz

def find_path(start, target, world):
    pos, time = [start], 0
    while target not in pos:
        world = update(world)
        next_pos = set()
        # for all currently valid positions
        for x, y in pos:
            for nx, ny in [(x, y), (x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (nx, ny) not in next_pos:
                    # list all surroundings that will be valid after bliz update
                    if valid(nx, ny, world):
                        next_pos.add((nx, ny))
        # update current valid positions
        pos = next_pos
        time += 1
    return time, world

time1, world = find_path((1, 0), (X-2, Y-1), data)
print(time1)
time2, world = find_path((X-2, Y-1), (1, 0), world)
time3, world = find_path((1, 0), (X-2, Y-1), world)
print(time1 + time2 + time3)