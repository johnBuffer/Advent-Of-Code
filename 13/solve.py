from functools import cmp_to_key
data, tl = [eval(x) for l in open('data.txt').read().split('\n\n') for x in l.split('\n')] + [[[6]], [[2]]], lambda x: x if type(x)==list else [x]

def comp(a, b):
    for x, y in zip(a, b):
        if (type(x) == type(y) == int):
            if x != y: return x < y
        elif comp(tl(x), tl(y)) is not None: return comp(tl(x), tl(y))
    if len(a) != len(b): return len(a) < len(b)

print(sum(i+1 for i, (a, b) in enumerate(data[2*i:2*i+2] for i in range(len(data)//2)) if comp(a, b)))
data.sort(key=cmp_to_key(lambda x, y: (-1 if comp(x, y) else 1)))
print((data.index([[2]]) + 1) * (1 + data.index([[6]])))