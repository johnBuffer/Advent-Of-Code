import time
data = [(-1 if c == '<' else 1) for l in open('data.txt') for c in l.strip()]
shapes = [l.strip().split('\n') for l in open('shapes.txt').read().split('\n\n')]


def create_rock(model, x, y):
    return [(x + a, y + len(model) - 1 - b) for b, l in enumerate(model) for a, c in enumerate(l) if c == '#']


def move_lat(rock, cave, dx):
    new_rock = [(x + dx, y) for x, y in rock]
    if all(-1 < x < 7 for x, _ in new_rock) and not any(c in cave for c in new_rock):
        return new_rock
    return rock


def move_down(rock, cave):
    new_rock = [(x, y - 1) for x, y in rock]
    return new_rock if all(y > -1 for _, y in new_rock) and not any(c in cave for c in new_rock) else rock


def rock(cave, obj, move, max_y):
    x, y = 2, max_y + 4
    rock = create_rock(shapes[obj], x, y)
    while True:
        rock = move_lat(rock, cave, data[move % len(data)])
        move = (move + 1) % len(data)
        if (next_rock := move_down(rock, cave)) == rock:
            return cave | set(rock), move, max(y for _, y in rock), rock
        rock = next_rock


def find_period_phase(cave):
    history, values, head, current_max, move, i = {}, {}, [-1] * 7, -1, 0, 0
    while True:
        top = tuple(current_max - y for y in head)
        key = (i % len(shapes), move, top)
        if key in history: return i - history[key], history[key], values
        else: history[key] = i
        cave, move, max_y, r = rock(cave, key[0], move, current_max)
        for a, b in r: head[a] = max(head[a], b)
        current_max = max(current_max, max_y)
        values[i], i = current_max, i + 1

cave = set((x, -1) for x in range(7))
period_i, phase_i, values = find_period_phase(cave)
def calc_height(target):
    loops = (target - phase_i) // period_i
    rest = (target - phase_i) - loops * period_i
    return loops * (values[period_i + phase_i - 1] - values[phase_i - 1]) + values[(rest + phase_i)]

print(calc_height(2022))
print(calc_height(1000000000000))