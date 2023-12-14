data = [list(l.strip()) for l in open('data.txt')]

def rotate(d):
    return list(zip(*d[::-1]))

def tilt(d):
    cpy = [list(l) for l in d]
    for i in range(len(d[0])):
        h = 0
        for k in range(len(cpy)):
            if cpy[k][i] == 'O':
                cpy[k][i], cpy[h][i], h = '.', 'O', h + 1
            elif cpy[k][i] == '#':
                h = k + 1
    return cpy

def cycle(d):
    for _ in range(4):
        d = rotate(tilt(d))
    return d

def get_mass(d):
    return sum(sum(c == 'O' for c in l) * (len(data) - i) for i, l in enumerate(d))

print(get_mass(tilt(data)))

histo, period, phase = {}, 0, 0
for c in range(1000000000):
    data = cycle(data)
    key = ''.join(''.join(l) for l in data)
    if key in histo:
        period = c - histo[key]
        phase = histo[key]
        break
    histo[key] = c

for c in range((1000000000 - len(histo) + period - 1) % period):
    data = cycle(data)

print(get_mass(data))
