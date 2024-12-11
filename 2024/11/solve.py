data, cache = [int(x) for x in open('input').read().strip().split(' ')], {}

def split(s):
    return [int(p) for p in [s[:len(s)//2], s[len(s)//2:]]]

def get(k):
    return cache.get(k) or cache.update({k: length(*k)}) or cache[k]

def length(x, i):
    return cache.get((x, i)) or 1 if not i else get((1, i-1)) if not x else sum(get((a, i-1)) for a in split(str(x))) if len(str(x)) % 2 == 0 else get((x * 2024, i-1))

print(sum(length(x, 25) for x in data))
print(sum(length(x, 75) for x in data))
