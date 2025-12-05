p1, p2 = open('input.txt').read().split('\n\n')
ranges = [[int(s) for s in r.split('-')] for r in p1.split('\n')]
ids = [int(i) for i in p2.split('\n')]

ranges = sorted(ranges, key=lambda x: x[0])
merged = [ranges[0]]
last = ranges[0][1]
for i in range(1, len(ranges)):
    a, b = ranges[i]
    if a <= last:
        if b > last:
            last = b
            merged[-1][1] = b
        else:
            # Nothing to do
            pass
    else:
        merged.append([a, b])
        last = b
ranges = merged

print(sum(any(a <= i <= b for a, b in ranges) for i in ids))
print(sum((b - a + 1) for a, b in merged))