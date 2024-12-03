import re

s = ''.join(open('data.txt'))
data = [([int(x) for x in m.groups()], m.span(0)) for m in re.finditer(r"mul\((\d+),(\d+)\)", s)]

def get_state(p):
    return s.rfind('do()', 0, p) >= s.rfind("don't()", 0, p)

print(sum(a * b for (a, b), _ in data))
print(sum(a * b for (a, b), (p, _) in data if get_state(p)))
