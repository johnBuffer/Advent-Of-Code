d = [[int(c) for c in l.strip()] for l in open('data.txt')]
w, h, t = len(d[0]), len(d), list(zip(*d))

def is_visible(x, y): return any(d[y][x] > v for v in [max(d[y][:x]), max(d[y][x+1:]), max(t[x][:y]), max(t[x][y+1:])])
def score(x, l): return sum(l[x] > max(l[i:x]) for i in range(x)) * (1 + sum(l[x] > max(l[x+1:i]) for i in range(x+2, w)))

print(2*(w+h)-4 + sum(is_visible(x, y) for y in range(1, h-1) for x in range(1, w-1)))
print(max(score(x, d[y]) * score(y, t[x]) for y in range(1, h-1) for x in range(1, w-1)))
