data = [l[5:][:-1] if '$' in l[0] else int(l.split(' ')[0]) for l in open('data.txt') if l[:3] != 'dir' and l[2:4] != 'ls']

def find_small(d): return sum(find_small(s) for s in d[0]) + d[1] * (d[1] < 100000)
def find_del(d, t): return min([find_del(s, t) for s in d[0]] + [d[1] if (d[1] >= t) else 70000000])
def build(i):
    subs, size = [], 0
    while i < len(data):
        if data[i] == '..': return i+1, [[subs, size]], size
        else: i, subs, size = (i+1, subs, size + data[i]) if type(data[i]) == int else [a+b for a, b in zip((0, subs, size), build(i+1))]
    return len(data), [[subs, size]], size

root, size = build(0)[1:]
print(find_small(root[0]))
print(find_del(root[0], size - 40000000))
