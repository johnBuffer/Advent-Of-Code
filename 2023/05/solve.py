data = [l.strip() for l in open('data.txt') if len(l) > 1]
seeds = [int(x) for x in data[0].split(' ') if x[0].isdigit()]
seeds_2 = [(a, a + b) for a, b in zip(seeds[0::2], seeds[1::2])]

def create(d, current, res):
    if not d:
        return res + [current]
    if d[0][0].isdigit():
        return create(d[1:], current + [[int(x) for x in d[0].split(' ')]], res)
    else:
        return create(d[1:], [], res + [current] if current else [])
maps = create(data, [], [])

def get_mapped(source, m, a, b, c):
    for l in m:
        if l[b] <= source < (l[b] + l[c]):
            return (source - l[b]) + l[a]
    return source

def is_valid(s):
    return any(a <= s <= b for a, b in seeds_2)

def compute(s, m, a, b, c):
    return compute(get_mapped(s, m[0], a, b, c), m[1:], a, b, c) if m else s

print(min(compute(s, maps, 0, 1, 2) for s in seeds))

idx, rmaps = 0, maps[::-1]
while True:    
    if is_valid(compute(idx, rmaps, 1, 0, 2)):
        print(idx)
        break
    idx += 1

