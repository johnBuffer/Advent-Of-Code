import math

def solve_2_lol(offsets):
    oc = [len(s) for s in ''.join([str(i) for i in offsets]).split('3') if len(s) > 1]
    return math.prod([[2, 4, 7][i-2] for i in oc])
    
data = [0] + sorted([int(l) for l in open('input')])
offsets = [data[i+1] - m for i, m in enumerate(data[:-1])] + [3]
# Problem 1
print(offsets.count(1) * offsets.count(3))
# Problem 2
print(solve_2_lol(offsets))
