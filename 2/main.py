input = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""
# with open("input.txt", "r") as fp:
#     input = fp.read()


def parse_input(i):
    return [[int(b) for b in a.split("-")] for a in i.split(",")]


def is_invalid(n, s):
    if n == "":
        return True
    if n.startswith(s):
        return is_invalid(n[len(s) :], s)
    return False


def check(n):
    substrings = []
    substring = ""
    for i in range(len(n) // 2):
        substring = n[0 : i + 1]
        substrings.append(substring)

    for substring in substrings:
        if is_invalid(n, substring):
            return int(n)
    return 0


sum = 0
for l, h in parse_input(input):
    for i in range(l, h + 1):
        # if n[: len(n) // 2] == n[len(n) // 2 :]:
        #     sum += i

        sum += check(str(i))

print(sum)
