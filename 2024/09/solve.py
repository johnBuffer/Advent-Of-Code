data = [int(x) for x in open('input').read().strip()]

def expand():
    return [[i//2 if i%2==0 else None for _ in range(x)] for i, x in enumerate(data) if x]

def merge(l, size = None):
    i = 0
    while i < (size or len(l)):
        if l[i][0] is None and l[i+1][0] is None:
            l[i] += l.pop(i+1)
        else:
            i += 1
    return l

def compact(l):
    i = -1
    while i > -len(l):
        if l[i][0] is not None:
            for k in range(-len(l), i):
                if l[k][0] is None:
                    size_s, size_cur = len(l[k]), len(l[i])
                    if size_s >= size_cur:
                        l[k] = l[i]
                        l[i] = [None] * size_cur
                        if size_s > size_cur:
                            l.insert(k+1, [None] * (size_s - size_cur))
                            i += 1
                        merge(l, i-1)
                        break
        i -= 1
    return l

def checksum(l):
    return sum(i * x for i, x in enumerate(l) if x)

print(checksum(y for s in compact(merge([[x] for l in expand() for x in l])) for y in s))
print(checksum(y for s in compact(expand()) for y in s))
