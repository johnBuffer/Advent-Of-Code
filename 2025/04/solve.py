data = {(x, y): c for y, l in enumerate(open('input.txt')) for x, c in enumerate(l.strip())}

def count2(x, y):
    return sum(data.get((dx, dy)) == '@' for dx in range(x-1, x+2) for dy in range(y-1, y+2) if dx != x or dy != y)

def remove_rolls():
    return [p for p, c in data.items() if c == '@' and count2(*p) < 4]

s, to_remove = 0, remove_rolls()
print(len(to_remove))
while to_remove:
    s += len(to_remove)
    for c in to_remove:
        data[c] = '.'
    to_remove = remove_rolls()

print(s)
