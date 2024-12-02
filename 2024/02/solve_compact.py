data = [[int(x) for x in l.strip().split(' ')] for l in open('data.txt')]
diff = lambda l: [a - b for a, b in zip(l, l[1:])]
valid = lambda l: all(-4 < x < 0 for x in diff(l)) or all(0 < x < 4 for x in diff(l))

print(sum(valid(l) for l in data))
print(sum(any(valid(x) for x in [l[:i] + l[i+1:] for i in range(len(l))] + [l]) for l in data))