data = [l.strip() for l in open('data.txt', 'r')]
num = [(str(i), i) for i in range(1, 10)]
num_alpha = [('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5), ('six', 6), ('seven', 7), ('eight', 8), ('nine', 9)]

def get_matches(s, token):
    # index + rindex
    return sorted([(s.index(n), x) for n, x in token if n in s] + [(s.rindex(n), x) for n, x in token if n in s])

def get_calib(matches):
    return matches[0][1] * 10 + matches[-1][1]

def get_sum(token):
    return sum(get_calib(get_matches(w, token)) for w in data)

print(get_sum(num))
print(get_sum(num_alpha + num))