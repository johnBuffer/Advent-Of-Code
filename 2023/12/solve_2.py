from collections import deque

def parse_line(l):
    a, b = l.strip().split()
    return a, tuple(int(x) for x in b.split(','))

data = [parse_line(l) for l in open('data.txt')]
data_2 = [('?'.join([a] * 5), 5 * b) for a, b in data]

def consume(v):
    copy = [x for x in v]
    copy[0] -= 1
    return copy

def remove_first(v):
    return [x for x in v][1:]

histo = {}
def solve(line, valid, count=0, current=''):
    if not line:
        return count + (sum(valid) == 0)
    else:
        last = current[-1] if current else ''
        h, r = line[0], line[1:]
        if len(valid) > 0:
            if h == '#':
                if valid[0] > 0:
                    return solve(r, consume(valid), count, current + h)
                return count
            elif h == '.':
                if last not in ['', '.']:
                    if valid[0] == 0:
                        return solve(r, remove_first(valid), count, current + h)
                    else:
                        return count
                else:
                    return solve(r, valid, count, current + h)
            elif h == '?':
                case_1 = solve('#' + r, valid, count, current)
                case_2 = solve('.' + r, valid, count, current)
                return case_1 + case_2
        else:
            return count + ('#' not in line)

print(sum(solve(a, b) for a, b in data_2))
