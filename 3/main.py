# input = """987654321111111
# 811111111111119
# 234234234234278
# 818181911112111"""
with open("input.txt", "r") as fp:
    input = fp.read()


def parse_input(i):
    return [[int(a) for a in n] for n in i.split()]


def find_max1(n):
    max1 = max(n[:-1])
    i = n.index(max1)
    max2 = max(n[i + 1 :])
    return int(str(max1) + str(max2))


def find_max2(n):
    res = ""
    searchspace = n
    i_min = -1
    for i_max in range(-11, 1):
        high = max(searchspace[: i_max or None])
        i_min = searchspace[: i_max or None].index(high)
        searchspace = searchspace[i_min + 1 :]
        res += str(high)
    return int(res)


def find_max(n, l):
    res = ""
    searchspace = n
    for i_max in range(-(l - 1), 1):
        high = max(searchspace[: i_max or None])
        i_min = searchspace[: i_max or None].index(high)
        searchspace = searchspace[i_min + 1 :]
        res += str(high)
    return int(res)


print(sum([find_max(n, 2) for n in parse_input(input)]))
print(sum([find_max(n, 12) for n in parse_input(input)]))
