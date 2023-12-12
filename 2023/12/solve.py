def parse_line(l, r):
    a, b = l.strip().split()
    return '?'.join([a] * r), [int(x) for x in b.split(',')] * r

def consume(v):
    return [x - (i==0) for i, x in enumerate(v)]

def solve(line, valid, histo, count=0, last=''):
    key = line, '_'.join(str(v) for v in valid)
    if key not in histo:
        if not line:
            histo[key] = count + (sum(valid) == 0)
        else:
            h, r = line[0], line[1:]
            if len(valid) > 0:
                if h == '#':
                    histo[key] = solve(r, consume(valid), histo, count, h) if valid[0] else count
                elif h == '.':
                    if last not in ['', '.']: # Entering a '.' section
                        histo[key] = count if valid[0] else solve(r, valid[1:], histo, count, h)
                    else: # Walking a '.' section
                        histo[key] = solve(r, valid, histo, count, h)
                elif h == '?':
                    histo[key] = solve('.' + r, valid, histo, count, last) + solve('#' + r, valid, histo, count, last)
            else:
                histo[key] = count + ('#' not in line)
    return histo[key]

print(sum(solve(a, b, {}) for a, b in [parse_line(l, 1) for l in open('data.txt')]))
print(sum(solve(a, b, {}) for a, b in [parse_line(l, 5) for l in open('data.txt')]))
