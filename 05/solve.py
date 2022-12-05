import re

data   = [l.replace('\n', '') for l in open('data.txt')]
stacks = [[l[i] for l in data if ('[' in l and l[i] != ' ')] for i in range(1, 37, 4)]
moves  = [(int(a), int(b)-1, int(c)-1) for a, b, c in [re.findall(r'\d+', l) for l in data if 'move' in l]]

def do_moves(m, s, func):
    for a, b, c in m: s[c], s[b] = func(s[b][:a]) + s[c], s[b][a:]
    return ''.join(l[0] for l in s)

print(do_moves(moves, [l for l in stacks], lambda x : x[::-1]))
print(do_moves(moves, [l for l in stacks], lambda x : x))

