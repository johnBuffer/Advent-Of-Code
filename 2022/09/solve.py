data, k1, k2 = [a for a, b in [l.strip().split(' ') for l in open('data.txt')] for _ in range(int(b))], [(0,0)]*2, [(0,0)]*10

def sign(x): return 1 if x > 0 else (-1 if x < 0 else 0)
def move(d, x, y): return (x + (d=='R') - (d=='L'), y + (d=='U') - (d=='D'))
def link(x, y, a, b): return (a + sign(x-a) * (abs(x-a)>1 or (abs(y-b)>1)), b + sign(y-b) * (abs(y-b)>1 or (abs(x-a)>1)))
def solve(knots, d):
    for i in range(len(knots)): knots[i] = link(*knots[i-1], *knots[i]) if i else move(d, *knots[i])

print(len(set((solve(k1, d), k1[-1]) for d in data)))
print(len(set((solve(k2, d), k2[-1]) for d in data)))