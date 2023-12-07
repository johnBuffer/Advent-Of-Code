data = [l.strip().split(' ') for l in open('data.txt')]

def joker(a):
    return max(a, key=a.get)

def replace(a, o='AKQT98765432'):
    return a.replace('J', joker({c: a.count(c) for c in o}))

def score(a, b, o='AKQJT98765432'):
    return [max(b.count(c) for c in b), -len(set(list(b)))] + [-o.index(c) for c in a]

def win(a):
    return sum(int(b) * (i + 1) for i, (_, b) in enumerate(a))

print(win(sorted(data, key=lambda x: score(x[0], x[0]))))
print(win(sorted(data, key=lambda x: score(x[0], replace(x[0]), 'AKQT98765432J'))))
