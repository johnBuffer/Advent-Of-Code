import re, math, copy

monkeys = []
for m in open('data.txt').read().split('\n\n'):
    l, r = m.split('\n'), []
    r.append([int(a) for a in l[1][18:].split(', ')])
    r += [l[2][19:]] + [int(a) for x in l[3:] for a in re.findall(r'\d+', x)]
    monkeys.append(r)
global_mod = math.prod(m[2] for m in monkeys)


def round(mks, count, division):
    times = [0] * len(mks)
    for _ in range(count):
        for idx, m in enumerate(mks):
            items, instr, div, t, f = m
            for i in [eval(instr)//division for old in items]: mks[f if i%div else t][0].append(i % global_mod)
            times[idx] += len(items)
            mks[idx][0] = []
    return sorted(times)[-2] * sorted(times)[-1]


print(round(copy.deepcopy(monkeys), 20, 3))
print(round(copy.deepcopy(monkeys), 10000, 1))
