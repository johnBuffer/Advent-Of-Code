import math

def snafu_digit(digit, power): return (-1 if digit == '-' else -2 if digit == '=' else int(digit)) * (5**power)
def snafu_to_int(snafu): return snafu_digit(snafu[0], len(snafu)-1) + snafu_to_int(snafu[1:]) if snafu else 0
def base5(n, p = None): return base5(n, int(math.log(n) / math.log(5))) if p is None else [] if p < 0 else [n // (5**p)] + base5(n % (5**p), p-1)
def int_to_snafu(number):
    res = [0] + base5(number)
    for i in range(len(res)-1, -1, -1):
        if   res[i] == 3: res[i], res[i-1] = '=', res[i-1] + 1
        elif res[i] == 4: res[i], res[i-1] = '-', res[i-1] + 1
        elif res[i] == 5: res[i], res[i-1] = 0  , res[i-1] + 1
    return (''.join(str(c) for c in res)).strip('0')

print(int_to_snafu(sum(snafu_to_int(l.strip()) for l in open('data.txt'))))