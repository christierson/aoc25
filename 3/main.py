# input = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""
with open("input.txt", "r") as fp:
    input = fp.read()


def parse_input(i):
    return [[int(a) for a in n] for n in i.split()]


def find_max(n):
    max1 = max(n[:-1])
    i = n.index(max1)
    max2 = max(n[i + 1 :])
    return int(str(max1) + str(max2))


def find_max2(n):
    res = ""
    searchspace = n
    i_min = -1
    for i_max in range(-11, 1, 1):
        high = max(searchspace[: i_max or None])
        i_min = searchspace[: i_max or None].index(high)
        searchspace = searchspace[i_min + 1 :]
        res += str(high)
    return int(res)


sum = 0
for n in parse_input(input):
    sum += find_max2(n)
print(sum)

# find_max2(parse_input(input)[2])


# 987654321111 + 811111111119 + 434234234278 + 888911112111 = 3121910778619
# 987654321111
# 811111111119
# 434444444478
# 888919192192
