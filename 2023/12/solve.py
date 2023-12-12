def parse_line(l):
    a, b = l.strip().split()
    return a, [int(x) for x in b.split(',')]

data = [parse_line(l) for l in open('data.txt')]

def is_valid(a, b):
    p = [x for x in a.split('.') if x]
    return len(p) == len(b) and all(len(s) == c for s, c in zip(p, b))

def get_possible(a, v, c='', count = 0):
    if a == '':
        return count + is_valid(c, v)
    else:
        h, r = a[0], a[1:]
        if h == '?':
            return get_possible(r, v, c + '.', count) + get_possible(r, v, c + '#', count)
        else:
            return get_possible(r, v, c + h, count)

print(sum(get_possible(a, v) for a, v in data))

data_2 = [('?'.join([a] * 5), 5 * b) for a, b in data]
for l in data_2:
    print(l)

