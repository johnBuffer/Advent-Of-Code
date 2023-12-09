data = [[int(x) for x in l.strip().split(' ')] for l in open('data.txt')]

def get(l, p=0):
    return [] if all(not x for x in l) else get([l[i+1] - l[i] for i in range(len(l) - 1)], p) + [l[p]]

def sum_back(l, res = 0):
    return sum_back(l[1:], l[0] - res) if l else res

print(sum(sum(get(l, -1)) for l in data))
print(sum(sum_back(get(l)) for l in data))
