data = [[int(x) for x in l.strip().split(' ') if x and x.isdigit()] for l in open('data.txt')]

def get_count(t, d):
    return sum(v * (t-v) > d for v in range(t))

def get_margin(d):
    return (get_count(*d[0]) * get_margin(d[1:]) if d else 1)

print(get_margin(list(zip(*data))))
print(get_margin([(int(''.join([str(x) for x in d])) for d in data)]))
