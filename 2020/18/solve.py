def get_closing(line, i, c = 1):
    return i-1 if not c else get_closing(line, i+1, c + (line[i] == '(') - (line[i] == ')'))
   
def apply_opt(opt, num, res, acc):
    return (res * acc, num) if opt == '*' else (res, acc + num)

def calc_1(expr):
    res, opt, nxt = 0, None, 0
    for i, c in enumerate(expr):
        if i < nxt: continue
        if c.isnumeric(): res = res * int(c) if opt == '*' else res + int(c)
        elif c == '(':
            closing = get_closing(expr, i+1)
            nxt, res = closing + 1, res * calc_1(expr[i+1:closing]) if opt == '*' else res + calc_1(expr[i+1:closing])
        else: opt = c
    return res
    
def calc_2(expr):
    res, acc, opt, nxt = 1, 0, None, 0
    for i, c in enumerate(expr):
        if i < nxt: continue
        if c.isnumeric(): res, acc = apply_opt(opt, int(c), res, acc)
        elif c == '(':
            closing = get_closing(expr, i+1)
            (res, acc), nxt = apply_opt(opt, calc_2(expr[i+1:closing]), res, acc), closing + 1
        else: opt = c
    return res * acc

data = [l.replace(' ', '').strip('\n') for l in open('input')]
# Part 1
print(sum(calc_1(s) for s in data))
# Part 2
print(sum(calc_2(s) for s in data))