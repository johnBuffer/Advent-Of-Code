data, boxes = open('data.txt').read().split(','), {i: [] for i in range(256)}

def hash(s, r = 0):
    return hash(s[1:], ((r + ord(s[0])) * 17) % 256) if s else r

def get_lens(box, label):
    return {l: i for i, (l, _) in enumerate(box)}.get(label, None)

for l in data:
    label, box, op = (l[:-1], hash(l[:-1]), '-') if '-' in l else (l[:-2], hash(l[:-2]), '=')
    index = get_lens(boxes[box], label)
    if op == '-' and index is not None:
        del boxes[box][index]
    elif op == '=':
        if index is not None:
            boxes[box][index][1] = int(l[-1])
        else:
            boxes[box].append([label, int(l[-1])])

print(sum(hash(l) for l in data))
print(sum((i + 1) * (k + 1) * f for i, v in boxes.items() for k, (_, f) in enumerate(v)))