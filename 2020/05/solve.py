def loadData(day):
	return [l.strip() for l in open('input', 'r')]

def dicho(data, up_char):
    return sum([int(c == up_char) * (2**(len(data) - 1 - i)) for i, c in enumerate(data)])

def get_seat_pos(seat_str):
    return dicho(seat_str[:7], 'B'), dicho(seat_str[7:], 'R')

def get_seat_id(seat_str):
    row, col = get_seat_pos(seat_str)
    return row * 8 + col

def solve_1():
    return max([get_seat_id(s) for s in loadData('05')])

def solve_2():
    # lel
    plane = ['0'] * 1024
    for s in loadData('05'):
        plane[get_seat_id(s)] = '1'
    
    return ''.join(plane).find('101') + 1

print(solve_1())
print(solve_2())
