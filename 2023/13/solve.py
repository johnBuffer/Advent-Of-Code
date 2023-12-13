data = [list(l.split('\n')) for l in open('data.txt').read().split('\n\n')]

def transpose(d):
    return [*zip(*d)]

def get_diff(a, b):
    return sum(x != y for x, y in zip(a, b))

def find_mirror(d, t):
    for i in range(len(d)-1):
        if sum(get_diff(d[i-k], d[i+1+k]) for k in range(i+1) if i+k+1 < len(d)) == t:
            return i + 1

def summarize(d, t):
    return (find_mirror(d, t) or 0) * 100 + (find_mirror(transpose(d), t) or 0)

print(sum(summarize(d, 0) for d in data))
print(sum(summarize(d, 1) for d in data))