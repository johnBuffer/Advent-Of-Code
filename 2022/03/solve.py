data = [[ord(c) - (38 if c <= 'Z' else 96) for c in l.strip()] for l in open('data.txt')]

def split(x, n) : return [x[n * i : n * i + n] for i in range(len(x)//n)]
print(sum(list(set(a) & set(b))[0] for a, b in [split(l, len(l)//2) for l in data]))
print(sum(list(set(a) & set(b) & set(c))[0] for a, b, c in split(data, 3)))
