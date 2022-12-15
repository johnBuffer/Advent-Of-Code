import re
def ext(x, y): return y[1] < x[0] or x[1] < y[0] # Are intervals disjoint
def fuse(x, y): return (min(x[0], y[0]) if x[0] <= y[1] else x[0]), (max(x[1], y[1]) if y[0] <= x[1] else x[1]) # Returns interval X fused with Y
def ins(i, o): return [o[0]] * ext(i, o[0]) + ins(fuse(i, o[0]), o[1:]) if o else [i] # Insert interval in list of fused intervals
def width(x, y, a, b, pos): return 2 * (abs(x - a) + abs(y - b) - abs(pos - y)) + 1
def count(Y, d, res): return count(Y, d[1:], ins([d[0][0] - c//2, d[0][0] + c//2 + 1], res) if (c := width(*d[0], Y)) > 0 else res) if d else res

data = [[int(x) for x in re.findall(r'-*\d+', l)] for l in open('data.txt')]
no = set((x, y) for _, _, x, y in data) | set((x, y) for x, y, _, _ in data)
print(len(set(c for x, y in count(2000000, data, []) for c in range(x, y) if (x, y) not in no)) - 1)
print([min(c[1] for c in l) * 4000000 + y for y, l in [[i, count(i, data, [])] for i in range(4000001)] if len(l) > 1][0])