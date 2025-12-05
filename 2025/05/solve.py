p1, p2 = open('input.txt').read().split('\n\n')
ranges = sorted([[int(s) for s in r.split('-')] for r in p1.split('\n')], key=lambda x: x[0])
ids = [int(i) for i in p2.split('\n')]

merged, last = [ranges[0]], ranges[0][1]
for i in range(1, len(ranges)):
    a, b = ranges[i]
    if a <= last and b > last:
        last, merged[-1][1] = b, b
    elif a > last:
        last, merged = b, merged + [[a, b]]
        last = b

print(sum(any(a <= i <= b for a, b in merged) for i in ids))
print(sum((b - a + 1) for a, b in merged))