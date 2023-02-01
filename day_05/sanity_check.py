
with open("day_05_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def make_stack():
    return [[],
            ['Q', 'M', 'G', 'C', 'L'],
            ['R', 'D', 'L', 'C', 'T', 'F', 'H', 'G'],
            ['V', 'J', 'F', 'N', 'M', 'T', 'W', 'R'],
            ['J', 'F', 'D', 'V', 'Q', 'P'],
            ['N', 'F', 'M', 'S', 'L', 'B', 'T'],
            ['R', 'N', 'V', 'H', 'C', 'D', 'P'],
            ['H', 'C', 'T'],
            ['G', 'S', 'J', 'V', 'Z', 'N', 'H', 'P'],
            ['Z', 'F', 'H', 'G']
            ]


with open("day_05_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def parse(line : str) -> list[int]:
    lst = line.split(" ")
    return [int(lst[1]), int(lst[3]), int(lst[5])]

def move_box(from_index : int, to_index : int, num : int, arr : list) -> None:
    for count in range(0, num):
        arr[to_index].append(arr[from_index].pop())

def move_boxes(from_index : int, to_index : int, num : int, arr : list) -> None:
    stack = []
    for count in range(0, num):
        stack.append(arr[from_index].pop())
    for count in range(0, num):
        arr[to_index].append(stack.pop())


stacks = make_stack()

for line in lines:
    my_arr = parse(line)
    move_box(my_arr[1], my_arr[2], my_arr[0], stacks)
out = ""
for x in range(1, len(stacks)):
    out += stacks[x].pop()
print(out)

stacks = make_stack()
for line in lines:
    my_arr = parse(line)
    move_boxes(my_arr[1], my_arr[2], my_arr[0], stacks)
out = ""
for x in range(1, len(stacks)):
    out += stacks[x].pop()
print(out)

