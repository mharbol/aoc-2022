
with open("day_06_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]


input = list(lines[0])

for start in range(0, len(input)):
    if len(set(input[start : start + 4])) == 4:
        print(start + 4)
        break

for start in range(0, len(input)):
    if len(set(input[start : start + 14])) == 14:
        print(start + 14)
        break



