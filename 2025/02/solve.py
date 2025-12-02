import re
data = [[int(n) for n in p.split('-')] for p in open('input.txt').read().strip().split(',')]
print(sum(n for a, b in data for n in range(a, b+1) if re.match(r'^(.+)\1$', str(n))))
print(sum(n for a, b in data for n in range(a, b+1) if re.match(r'^(.+)\1+$', str(n))))