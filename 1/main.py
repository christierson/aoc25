def parse_instruction(input):
    direction, distance = input[0], input[1:]
    if direction == "L":
        return int(distance), -1
    else:
        return int(distance), 1


def spin(value, direction, distance):
    zeropass = distance // 100
    change = (distance - zeropass * 100) * direction
    new = value + change
    if (new < 0 or new > 100) and value != 0:
        zeropass += 1
    new = new % 100
    if new == 0:
        zeropass += 1
    return new, zeropass


with open("input.txt", "r") as fp:
    input = fp.read()

# input = """L68
# L30
# R48
# L5
# R60
# L55
# L1
# L99
# R14
# L82"""

ptr = 50
code = 0
for i in input.split():
    distance, direction = parse_instruction(i)
    ptr, n = spin(ptr, direction, distance)
    code += n

print(code)
