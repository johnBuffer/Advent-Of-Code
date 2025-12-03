data = [[int(c) for c in l.strip()] for l in open('input.txt')]

def imax(v): return (m := max(v)), v.index(m)

def get_rec(b, count, i, res):
    if i == count:
        return res
    a, ai = imax(b[:len(b) - count + i + 1])
    return get_rec(b[ai+1:], count, i + 1, res * 10 + a)

print(sum(get_rec(b, 2, 0, 0) for b in data))
print(sum(get_rec(b, 12, 0, 0) for b in data))