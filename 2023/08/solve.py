instr, rest = open('data.txt').read().split('\n\n')
net = {l[:3]: (l[7:10], l[12:15]) for l in rest.split('\n')}

def walk(x, condition, c=0):
    while not condition(x): c, x = c + 1, net[x][instr[c % len(instr)] == 'R']
    return c

def first_prime(x, i=2):
    return i if (x % i == 0) and all(i % k for k in range(2, i)) else first_prime(x, i + 1)

def get_primes(x, res):
    return res if x < 2 else get_primes(x // first_prime(x), res + [first_prime(x)])

def mult(f, res=1, i=0):
    return mult(f, res * list(f)[i], i + 1) if i < len(f) else res

print(walk('AAA', lambda x: x == 'ZZZ'))
print(mult(set(p for x in [walk(s, lambda x: x[2] == 'Z') for s in net if s[2] == 'A'] for p in get_primes(x, []))))

