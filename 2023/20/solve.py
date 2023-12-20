import math, collections

def get_name(a):
    return a[1:] if a[0] in '%&' else a

def get_type(a):
    return 'flip' if a[0] == '%' else ('conj' if a[0] == '&' else 'broad')

def get_upstream(name):
    return [m for m, (o, _, _) in data.items() if name in o]

data = {get_name(a): [b.split(', '), get_type(a), False]  for a, b in [l.strip().split(' -> ') for l in open('data.txt')]}
inputs = {a: {b: 0 for b in get_upstream(a)} for a in data}
upstream = get_upstream(get_upstream('rx')[0])
iteration, period = 0, [[0, 0] for _ in upstream]

def update_period(name):
    if name in upstream:
        cur = upstream.index(name)
        if period[cur][0] == 0:
            period[cur][0] = iteration
        else:
            period[cur][1] = iteration - period[cur][0]

def update_inputs(from_, to_, sig):
    if to_ in data:
        inputs[to_][from_] = sig
        _, kind, state = data[to_]
        if kind == 'flip' and sig == 0:
            data[to_][2] = not state
            return (to_, not state)
        elif kind == 'conj':
            if all(i == 1 for i in inputs[to_].values()):
                return (to_, 0)
            else:
                update_period(to_)
                return (to_, 1)

def send_pulse():
    to_send = collections.deque([('broadcaster', 0)])
    l, h = 1, 0
    while to_send:
        name, sig = to_send.pop()
        out, _, _ = data[name]
        for o in out:
            l, h, a = l + 1 - sig, h + sig, update_inputs(name, o, sig)
            to_send += [a] if a else []
    return l, h

sum_low = sum_high = 0
for _ in range(1000):
    l, h = send_pulse()
    sum_low, sum_high = sum_low + l, sum_high + h
print(sum_low * sum_high)

while any(not p for _, p in period):
    send_pulse()
    iteration += 1
print(math.lcm(*[p for _, p in period]))