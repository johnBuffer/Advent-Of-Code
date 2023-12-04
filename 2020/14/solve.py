def parse(line):
    (l, r), a = line.strip('\n').split(' = '), line.find('mask') == -1
    return int(l[4 : -1]) if a else None, int(r) if a else None, r if not a else None

def write_mem(address, value, mask, index, memory):
    if index == len(mask):
        memory[address] = value
    else:
        bitmask = int(mask[index] != '0') << (35 - index)
        write_mem(address | bitmask, value, mask, index + 1, memory)
        if mask[index] == 'X':
            write_mem((address | bitmask) ^ bitmask, value, mask, index + 1, memory)

def solve_1(data):
    mask, memory = 'X'*36, {}
    for addr, val, msk in data:
        mask = msk if msk else mask
        if addr:
            val_bits = [(val//(2**(35 - i)))%2 if mask[i] == 'X' else int(mask[i]) for i in range(36)]
            memory[addr] = sum([b * (2**(35 - i)) for i, b in enumerate(val_bits)])
    return sum(v for v in memory.values())

def solve_2(data):
    mask, memory = '0'*36, {}
    for addr, val, msk in data:
        mask = msk if msk else mask
        if addr:
            write_mem(addr, val, mask, 0, memory)
    return sum(v for v in memory.values())

data = [parse(l) for l in open('input')]
print(solve_1(data))
print(solve_2(data))
