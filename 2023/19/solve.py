def parse(l):
    name, rest = l.split('{')
    conditions = rest[:-1].split(',')
    return name, conditions

rules_raw, data_raw = open('data.txt').read().split('\n\n')
rules = {n: c for n, c in [parse(l) for l in rules_raw.split('\n\n')[0].split('\n')]}
data, res = [(l[1:-1].replace(',', ';')) for l in data_raw.split('\n')], []

accepted = []
for l in data:
    x = m = a = s = 0
    exec(l)
    current = 'in'
    while current:
        r = rules[current]
        for c in r:
            if ':' in c:
                test, then = c.split(':')
                if eval(test):
                    if then == 'A':
                        accepted.append((x, m, a, s))
                        current = None
                        break
                    elif then == 'R':
                        current = None
                        break
                    else:
                        current = then
                        break
            elif c == 'A':
                accepted.append((x, m, a, s))
                current = None
            elif c == 'R':
                current = None
            else:
                current = c

print(sum(sum(l) for l in accepted))

def split(rng, value, op):
    if op == '<':
        s, f = [rng[0], min(rng[1], value - 1)], [max(rng[0], value), rng[1]]
    else:
        f, s = [rng[0], min(rng[1], value)], [max(rng[0], value + 1), rng[1]]
    return s, f

def process_range(ranges, current, res):
    for c in current:
        if c == 'A':
            res.append(ranges)
        elif c != 'R':
            if ':' not in c:
                process_range(ranges, rules[c], res)
            else:
                test, then = c.split(':')
                op = '<' if '<' in test else '>'
                arg, value = test.split(op)
                arg_i = 'xmas'.index(arg)
                success, fail = split(ranges[arg_i], int(value), op)
                next_ranges = [r if i != arg_i else success for i, r in enumerate(ranges)]
                if then == 'A':
                    res.append(next_ranges)
                elif then != 'R':
                    process_range(next_ranges, rules[then], res)
                ranges[arg_i] = fail

def count(r):
    return (r[0][1] - r[0][0] + 1) * count(r[1:]) if len(r) else 1

process_range([[1, 4000] for _ in range(4)], rules['in'], res)
print(sum(count(r) for r in res))
