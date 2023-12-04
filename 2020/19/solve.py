import re

def load_data():
    rules_data, words_data = open('input').read().split('\n\n')
    return parse_rules(rules_data), [w for w in words_data.split('\n')]

def parse_rules(data):
    rules = {}
    for l in data.split('\n'):
        left, right = l.split(': ')
        if right[0] == '"': rules[left] = right[1], [], []
        elif '|' in right:
            or_left, or_right = right.split(' | ')
            rules[left] = None, or_left.split(' '), or_right.split(' ')
        else:
            rules[left] = None, right.split(' '), []
    return rules

def gen(rule, rules, deep=0):
    if deep < 15: # my humble solution for part 2 xD
        char, left, right = rules[rule]
        if char is not None: 
            return char
        parts = [''.join([gen(r, rules, deep + 1) for r in p]) for p in [left, right]]
        if not all(len(p) == 0 for p in parts):
            reg = '|'.join([p for p in parts if len(p)])
            return reg if not right else '({})'.format(reg)
    return ''

rules, words = load_data()
regex_data = '^{}$'.format(gen('0', rules))
print(regex_data)
# Part 1 and 2
regex = re.compile(regex_data)
print(sum(bool(regex.match(w)) for w in words))
