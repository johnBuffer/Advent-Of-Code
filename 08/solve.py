d = [[int(c) for c in l.strip()] for l in open('data.txt')]
w, h = len(d[0]), len(d)

visible = 0
for x in range(len(d[0])):
    for y in range(len(d)):
        current = d[y][x]

        if (x == 0 or y == 0 or x == len(d[0]) - 1 or y == len(d) -1):
            visible += 1
        else:
            left = max(d[y][:x]) < current
            right = max(d[y][x+1:]) < current
            top   = max(d[i][x] for i in range(0, y)) < current
            bottom   = max(d[i][x] for i in range(y + 1, len(d))) < current
            visible += left or right or top or bottom


best = 0
for x in range(len(d[0])):
    for y in range(len(d)):
        current = d[y][x]

        if (x == 0 or y == 0 or x == len(d[0]) - 1 or y == len(d) -1):
            pass
        else:
            left = 0
            for xx in range(x-1, -1, -1):
                if d[y][xx] < current:
                    left += 1
                if d[y][xx] >= current:
                    left += 1
                    break

            right = 0
            for xx in range(x+1, len(d[0])):
                if d[y][xx] < current:
                    right += 1
                if d[y][xx] >= current:
                    right += 1
                    break
            
            top = 0
            for yy in range(y-1, -1, -1):
                if d[yy][x] < current:
                    top += 1
                if d[yy][x] >= current:
                    top += 1
                    break

            down = 0
            for yy in range(y+1, len(d)):
                if d[yy][x] < current:
                    down += 1
                if d[yy][x] >= current:
                    down += 1
                    break

            if x == 2 and y == 3:
                print(current, down, top, left, right)

            best = max(best, down * top * left * right)


print(visible)
# print(2*(w+h)-4 + sum(any(d[y][x] > v for v in [max(d[y][:x]), max(d[y][x+1:]), max(d[i][x] for i in range(y)), max(d[i][x] for i in range(y + 1, h))]) for y in range(1, h-1) for x in range(1, w-1)))



print(best)
