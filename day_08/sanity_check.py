
with open("day_08_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

array = []

for line in lines:
    array.append([int(digit) for digit in line])

VERBOSE = False

def is_visible(x, y, array):
    # base cases:
    if x == 0:
        return 1
    if y == 0:
        return 1
    if x == len(array) - 1:
        return 1
    if y == len(array) - 1:
        return 1
    # actual meat of it
    if vis_from_right(x, y, array):
        return 1
    if vis_from_left(x, y, array):
        return 1
    if vis_from_top(x, y, array):
        return 1
    if vis_from_bottom(x, y, array):
        return 1
    return 0

def vis_from_left(x, y, array):
    for i in range(0, x):
        if array[i][y] >= array[x][y]:
            return False
    return True

def vis_from_right(x, y, array):
    for i in range(len(array) - 1, x, -1):
        if array[i][y] >= array[x][y]:
            return False
    return True

def vis_from_top(x, y, array):
    for i in range(0, y):
        if array[x][i] >= array[x][y]:
            return False
    return True

def vis_from_bottom(x, y, array):
    for i in range(len(array) - 1, y, -1):
        if array[x][i] >= array[x][y]:
            return False
    return True


tot = 0
for x in range(len(array)):
    for y in range(len(array)):
        tot += is_visible(x, y, array)


scenic_scores = [[0] * 99] * 99


def score_north(x, y, array):

    if y == 0:
        return 0
    for i in range(y - 1, -1, -1):
        if array[x][i] >= array[x][y]:
            return y - i
    return y

def score_south(x, y, array):
    if y == 98:
        return 0
    for i in range(y + 1, 99):
        if array[x][i] >= array[x][y]:
            return i - y
    return 98 - y

def score_west(x, y, array):
    if x == 0:
        return 0
    for i in range(x - 1, -1, -1):
        if array[i][y] >= array[x][y]:
            return x - i
    return x

def score_east(x, y, array):
    if x == 98:
        return 0
    for i in range(x + 1, 99):
        if array[i][y] >= array[x][y]:
            return i - x
    return 98 - x


maxes = []

for a in range(99):
    for b in range(99):
        maxes.append(score_north(a, b, array) * score_south(a, b, array) * score_west(
            a, b, array) * score_east(a, b, array))

print(max(maxes))

