import re
data = [[int(n) for n in p.split('-')] for p in open('input.txt').read().strip().split(',')]

pattern_1, pattern_2 = re.compile(r'^(.+)\1$'), re.compile(r'^(.+)\1+$')
def is_invalid_re(n, part_2):
    return re.match(pattern_2 if part_2 else pattern_1, str(n))

print(sum(n for a, b in data for n in range(a, b+1) if is_invalid_re(n, False)))
print(sum(n for a, b in data for n in range(a, b+1) if is_invalid_re(n, True)))