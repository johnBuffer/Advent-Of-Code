m = [[int(c) for c in l.strip()] for l in open('input')]
X, Y, valid = len(m[0]), len(m), lambda x, y, i: 0 <= x < X and 0 <= y < Y and m[y][x] == i+1

def w(x, y, i=-1):
    return (w(x-1, y, i+1) + w(x, y-1, i+1) + w(x+1, y, i+1) + w(x, y+1, i+1) if m[y][x] != 9 else [(x, y)]) if valid(x, y, i) else []

print(sum(len(set(w(x, y))) for x in range(X) for y in range(Y)))
print(sum(len(w(x, y)) for x in range(X) for y in range(Y)))
