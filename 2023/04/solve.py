import re

scores = [35 - len(set(re.findall(r'(\d+)', l)[1:])) for l in open('data.txt')]

def play(i=0, r={}):
    return r[i] if i in r else 1 + sum(play(i + x + 1) for x in range(scores[i]))

print(sum(int(2**(x - 1)) for x in scores))
print(sum(play(i) for i in range(len(scores))))
