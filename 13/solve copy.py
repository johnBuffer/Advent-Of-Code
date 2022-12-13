data = [[eval(x) for x in l.split('\n')] for l in open('data.txt').read().split('\n\n')]
    
def comp(i, a, b):
    for x, y in zip(a, b):
        if type(x) == type(y):
            if type(x) == int: return 1 if x < y else (x == y) * 2
            else:
                r = comp(i, x, y)
                if r != 3: return r
        else:
            r = comp(i, [x], y) if type(x) == int else comp(i, x, [y])
            if r != 3: return r
    return comp(i, len(a), len(b))


print(sum(i+1 for i, (a, b) in enumerate(data) if comp(i+1, a, b)))

p = [x for l in data for x in l] + [[[2]], [[6]]]
r = []
while p:
    for i, x in enumerate(p):
        if all(comp(0, x, y) for y in p[:i] + p[i+1:]):
            r.append(x)
            p = p[:i] + p[i+1:]
            break

print((r.index([[2]]) + 1) * (1 + r.index([[6]])))


