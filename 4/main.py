# input = """..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# """

with open("input.txt", "r") as fp:
    input = fp.read()


def adjacent(grid, x, y):
    sum = 0
    for i in [a for a in range(y - 1, y + 2) if 0 <= a < len(grid)]:
        for j in [a for a in range(x - 1, x + 2) if 0 <= a < len(grid[i])]:
            if i == y and j == x:
                continue
            sum += grid[i][j]
    return sum


grid = [[int(c == "@") for c in line] for line in input.split()]

total = 0
while sum != 0:
    sum = 0
    for y, row in enumerate(grid):
        for x, p in enumerate(row):
            if not p:
                continue

            if adjacent(grid, x, y) < 4:
                grid[y][x] = 0
                sum += 1
    total += sum

print(total)
