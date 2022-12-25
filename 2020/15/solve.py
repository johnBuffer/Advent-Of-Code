def solve(data, count):
    histo, last = {int(l): i for i, l in enumerate(data)}, data[-1]
    for i in range(len(histo), count):
        histo[last], last = i-1, i-1 - histo.get(last, i-1)
    return last

input = [int(l) for l in open('input')]
# Part 1
print(solve(input, 2020))
# Part 2
print(solve(input, 30000000))