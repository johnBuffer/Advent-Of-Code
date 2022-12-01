data = [[int(v) for v in l.split('\n')] for l in open('data.txt').read().split('\n\n')]
sums = sorted([sum(l) for l in data])

print(sums[-1])
print(sum(sums[-3:]))
