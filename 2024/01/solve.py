data = [int(x) for l in open('data.txt') for x in l.strip().split('   ')]

print(sum(abs(a - b) for a, b in zip(sorted(data[::2]), sorted(data[1::2]))))
print(sum(a * data[1::2].count(a) for a in (data[::2])))
