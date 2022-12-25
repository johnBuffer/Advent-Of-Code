data = [[({'X':1,'Y':2,'Z':3,'A':1,'B':2,'C':3}[v] - 1) for v in l.strip().split(' ')] for l in open('data.txt')]

print(sum((b + 1 + (3 * (a == b) + 6 * (b == (a + 1) % 3))) for a, b in data))
print(sum((1 + ((a - 1) % 3 if b == 0 else a + 3 if b == 1 else (a + 1) % 3 + 6)) for a, b in data))        
