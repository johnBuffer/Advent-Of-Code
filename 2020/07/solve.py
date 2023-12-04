def parseRule(line):
    # Remove the dot
    parts = line.strip('\n')[:-1].split('bags contain')
    subs = []
    if parts[1].find("no other bags") == -1:
        for s in parts[1].split(','):
            count, bag = s.strip().split(' ', 1)
            subs.append((int(count), bag[:bag.rfind(' ')]))
    return parts[0].strip(), subs

def canContain(outer, inner, rules):
    return sum(b == inner or canContain(b, inner, rules) for _, b in rules[outer]) > 0

def count(bag, rules):
    return sum(c * (count(b, rules) + 1) for c, b in rules[bag])

rules = dict(parseRule(l) for l in open('input'))
# Problem 1
print(sum(canContain(r, "shiny gold", rules) for r in rules.keys()))
# Problem 2
print(count("shiny gold", rules))
