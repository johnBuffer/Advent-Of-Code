def parse_line(line):
	parts = line.split(' ')
	times_low = int(parts[0].split('-')[0])
	times_up = int(parts[0].split('-')[1])
	letter = parts[1][0]
	password = parts[2]

	return times_low, times_up, letter, password

def loadData():
	return [parse_line(l) for l in open("input", "r")]

def solve_1():
	data = loadData()
	result = 0
	for times_low, times_up, letter, password in data:
		if times_up >= password.count(letter) >= times_low:
			result += 1

	return result

def solve_2():
	data = loadData()
	result = 0
	for times_low, times_up, letter, password in data:
		if password[times_low - 1] == letter and password[times_up - 1] != letter:
			result += 1
		elif password[times_low - 1] != letter and password[times_up - 1] == letter:
			result += 1

	return result

print(solve_2())