alpha = 'abcdefghijklmnopqrstuvwxyz'

def loadAllData(day):
    return open('input', 'r').read()

def solve_1():
    groups = loadAllData('06').split('\n\n')
    return sum([len(set([l for l in g if l in alpha])) for g in groups])

def solve_2():
    groups = [(g, g.count('\n') + 1) for g in loadAllData('06').split('\n\n')]
    return sum([sum([g.count(letter) == c for letter in alpha]) for g, c in groups])

print(solve_1())
print(solve_2())
