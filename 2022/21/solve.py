data = [l.strip() for l in open('data.txt')]
monkeys = {name: int(rest) if len(ps := rest.split(' ')) == 1 else ps for name, rest in [l.split(': ') for l in data]}

def calc_value(m, monkeys):
    history, queue = {}, [m]
    while queue:       
        current, queue = queue[0], queue[1:]
        if isinstance(monkeys[current], int): history[current] = monkeys[current]
        else:
            d1, op, d2 = monkeys[current]
            if d1 in history and d2 in history: history[current] = eval('int(history["{}"]{}history["{}"])'.format(d1, op, d2))
            else: queue += [current] + [x for x in [d1, d2] if all(x not in y for y in [queue, history])]
    return history[m]

def calc_value_human(m, monkeys, target_value):
    if m == 'humn': return target_value
    d1, op, d2 = monkeys[m]
    if human(d1, monkeys, set()):
        other_value, target = calc_value(d2, monkeys), 0
        if op == '-':   target = target_value + other_value
        elif op == '+': target = target_value - other_value
        elif op == '*': target = int(target_value / other_value)
        else:           target = int(other_value * target_value)
        return calc_value_human(d1, monkeys, target)
    elif human(d2, monkeys, set()):
        other_value, target = calc_value(d1, monkeys), 0
        if op == '-':   target = -(target_value - other_value)
        elif op == '+': target = (target_value - other_value)
        elif op == '*': target = int(target_value / other_value)
        else:           target = int(other_value / target_value)
        return calc_value_human(d2, monkeys, target)

def human(m, ms, res):
    if isinstance(ms[m], int):
        return m == 'humn' or 'humn' in res
    (d1, _, d2), deps = ms[m], res | set([ms[m][0], ms[m][2]])
    return human(d1, ms, deps) or human(d2, ms, deps)

print(calc_value('root', monkeys))
print(calc_value_human(monkeys['root'][0], monkeys, calc_value(monkeys['root'][2], monkeys)))