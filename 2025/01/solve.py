data = [int(l.strip().replace('L', '-').replace('R', '')) for l in open('input.txt')]

def get_count(part_2 = False):
    count, tick = 0, 50
    for d in data:
        s = 1 if d > 0 else -1
        for i in range(s * d):
            tick = (tick + s) % 100
            count += (not tick) and (part_2 or i == (abs(d) - 1))
    return count

print(get_count())
print(get_count(True))