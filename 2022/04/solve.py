data = [[int(n) for p in l.strip().split(',') for n in p.split('-')] for l in open('data.txt')]

print(sum((a >= c and b <= d) or (c >= a and d <= b) for a, b, c, d in data))
print(sum(len(set(range(a, b + 1)) & set(range(c, d + 1))) > 0 for a, b, c, d in data))
