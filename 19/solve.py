import re

data = [[int(x) for x in re.findall('\d+', l)][1:] for l in open('data.txt')]

hist = {}
def calc(time, costs, r_or, r_cl, r_ob, r_ge, c_or, c_cl, c_ob, c_ge):
    time -= 1
    if time == 0:
        return c_ge + r_ge

    key = (time, r_or, r_cl, r_ob, r_ge, c_or, c_cl, c_ob, c_ge)
    if key in hist:
        return hist[key]
    
    max_geode, build = 0, 0
    if costs[0] <= c_or:
        geode = calc(time, costs, r_or + 1, r_cl, r_ob, r_ge, c_or + r_or - costs[0], c_cl + r_cl, c_ob + r_ob, c_ge + r_ge)
        max_geode, build = max(max_geode, geode), build + 1
    if costs[1] <= c_or:
        geode = calc(time, costs, r_or, r_cl + 1, r_ob, r_ge, c_or + r_or - costs[1], c_cl + r_cl, c_ob + r_ob, c_ge + r_ge)
        max_geode, build = max(max_geode, geode), build + 1
    if costs[2] <= c_or and costs[3] <= c_cl:
        geode = calc(time, costs, r_or, r_cl, r_ob + 1, r_ge, c_or + r_or - costs[2], c_cl + r_cl - costs[3], c_ob + r_ob, c_ge + r_ge)
        max_geode, build = max(max_geode, geode), build + 1
    if costs[4] <= c_or and costs[5] <= c_ob:
        geode = calc(time, costs, r_or, r_cl, r_ob, r_ge + 1, c_or + r_or - costs[4], c_cl + r_cl, c_ob + r_ob - costs[5], c_ge + r_ge)
        max_geode, build = max(max_geode, geode), build + 1
    if build < 4:
        geode = calc(time, costs, r_or, r_cl, r_ob, r_ge, c_or + r_or, c_cl + r_cl, c_ob + r_ob, c_ge + r_ge)
        max_geode, build = max(max_geode, geode), build + 1

    hist[key] = max_geode
    return max_geode

res = 0
for i, costs in enumerate(data):
    hist = {}
    geode = calc(24, costs, 1, 0, 0, 0, 0, 0, 0, 0)
    res += (i + 1) * geode
print(res)

res = 0
for i, costs in enumerate(data[:3]):
    hist = {}
    geode = calc(32, costs, 1, 0, 0, 0, 0, 0, 0, 0)
    res += (i + 1) * geode
print(res) # Sorry RAM :(