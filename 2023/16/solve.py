data = [l.strip() for l in open('data.txt')]

def is_valid(x, y):
    return 0 <= x < len(data[0]) and 0 <= y < len(data)

def energize(s, d):
    to_process, visited = [[*s, *d]], set()
    while to_process:
        state = to_process.pop()
        while is_valid(*state[:2]) and tuple(state) not in visited:
            x, y, vx, vy = state
            visited.add(tuple(state))
            if data[y][x] not in '.|-':
                vx, vy = (-vy, -vx) if data[y][x] == '/' else (vy, vx)
            elif data[y][x] == '|' and vx:
                to_process += [(x, y + 1, 0,  1), (x, y - 1, 0, -1)]
                break
            elif data[y][x] == '-' and vy:
                to_process += [(x + 1, y, 1, 0), (x - 1, y, -1, 0)]
                break
            state = (x + vx, y + vy, vx, vy)
    return len(set((x, y) for x, y, _, _ in visited))

print(energize((0, 0), (1, 0)))
X, Y = len(data[0]), len(data)
starts  = [((x, y), (0, vy)) for x in range(X) for y, vy in [(0, 1), (Y-1, -1)]]
starts += [((x, y), (vx, 0)) for y in range(Y) for x, vx in [(0, 1), (X-1, -1)]]
print(max(energize(p, d) for p, d in starts))