data = [[int(x) for x in l.strip().split(' ')] for l in open('data.txt')]

def check(l, rule):
    return all(rule(a, b) for a, b in zip(l, l[1:]))

def is_valid(l):
    return (check(l, lambda a, b: b+4 > a > b) or check(l, lambda a, b: a+4 > b > a))

def remove_1(l):
    return [l[:i] + l[i+1:] for i in range(len(l))]

print(sum(is_valid(l) for l in data))
print(sum(any(is_valid(x) for x in remove_1(l)) or is_valid(l) for l in data))
