data = [[[int(x) for x in n.split(' ') if x] for n in p.split(' | ')] for l in open('data.txt') for p in l.strip().split(': ')[1]]

print(data)

#print(2**(sum(x in y) for x, y in ))