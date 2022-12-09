data = [a for a, b in [l.strip().split(' ') for l in open('data.txt')] for _ in range(int(b))]

def sign(x): return 1 if x > 0 else (-1 if x < 0 else 0)
def move(d, x, y): return (x + (d=='R') - (d=='L'), y + (d=='U') - (d=='D'))
def link(x, y, a, b): return (a + sign(x-a) * (abs(x-a)>1 or (abs(y-b)>1)), b + sign(y-b) * (abs(y-b)>1 or (abs(x-a)>1)))

def solve(l):
    knots, explored = [(0, 0)] * l, set()
    for d in data:
        for i in range(l): knots[i] = link(*knots[i-1], *knots[i]) if i else move(d, *knots[i])
        explored.add(knots[-1])
    return(len(explored))

print(solve(2))
print(solve(10))