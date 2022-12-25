data = open('data.txt').read().strip()

def find_pattern(n): return [i+n for i in range(len(data) - n) if len(set(c for c in data[i:i+n])) == n][0]
print(find_pattern(4))
print(find_pattern(14))