data = [[int(x) for x in l.strip().replace(':', '').split(' ')] for l in open('input')]
ops = [lambda a, b: a+b, lambda a, b: a*b, lambda a, b: int(str(a)+str(b))]

def is_valid(t, n, ops, s=0):
    return any(is_valid(t, n[1:], ops, o(s, n[0])) for o in ops) if n else s==t

print(sum(l[0] for l in data if is_valid(l[0], l[1:], ops[:2])))
print(sum(l[0] for l in data if is_valid(l[0], l[1:], ops)))