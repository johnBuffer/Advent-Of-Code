xs, ys = [1, 0, -1, 0], [0, 1, 0, -1]

def parse(line):
    c, a = 'EWSNFRL'.index(line[:1]), int(line[1:])
    return a * ((c == 0) - (c == 1)), a * ((c == 2) - (c == 3)), (c == 4) * a, (a//90) * ((c == 5) - (c == 6))

def solve_1(data, x, y, a):
    for dx, dy, df, da in data:
        x, y, a = x + dx + xs[a] * df, y + dy + ys[a] * df, (a + da)%4
    return abs(x) + abs(y)

def solve_2(data, x, y, wx, wy):
    for dx, dy, df, a in data:
        x, y, wx, wy = x + wx * df, y + wy * df, wx * xs[a%4] - wy * ys[a%4] + dx, wx*ys[a%4] + wy * xs[a%4] + dy 
    return abs(x) + abs(y)

input = [parse(l) for l in open('input')]
print(solve_1(input, 0, 0, 0))
print(solve_2(input, 0, 0, 10, -1))
