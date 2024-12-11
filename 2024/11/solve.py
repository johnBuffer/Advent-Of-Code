data, cache = [int(x) for x in open('input').read().strip().split(' ')], {}

def split(s):
    return [int(p) for p in [s[:len(s)//2], s[len(s)//2:]]]

def mut(x):
    return [1] if not x else split(str(x)) if len(str(x)) % 2 == 0 else [x*2024]

def get(k):
    return cache.get(k) or cache.update({k: length(*k)}) or cache[k]

def length(x, i):
    return cache.get((x, i)) or 1 if not i else sum(get((n, i-1)) for n in mut(x))

print(sum(length(x, 25) for x in data))
print(sum(length(x, 75) for x in data))
