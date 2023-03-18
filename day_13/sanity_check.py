
from nested_list_tree import NestedListComparitor

with open("day_13_input.txt") as file:
    real_input = [line.strip() for line in file.readlines()]

test_input = [
    "[1,1,3,1,1]", "[1,1,5,1,1]", "",
    "[[1],[2,3,4]]", "[[1],4]", "",
    "[9]", "[[8,7,6]]", "",
    "[[4,4],4,4]", "[[4,4],4,4,4]", "",
    "[7,7,7,7]", "[7,7,7]", "",
    "[]", "[3]", "",
    "[[[]]]", "[[]]", "",
    "[1,[2,[3,[4,[5,6,7]]]],8,9]", "[1,[2,[3,[4,[5,6,0]]]],8,9]"
]

# Assign the correct array
input_array = real_input

# Part 1
lines = [NestedListComparitor(line) for line in list(filter(lambda entry : entry != "", input_array))]

correct = []
for index in range(0, len(lines), 2):
    if lines[index] < lines[index + 1]:
        correct.append(index // 2 + 1)
print(sum(correct))

# Part 2
# Making my stupid structure finally worked for the better
marker_2 = NestedListComparitor("[[2]]")
marker_6 = NestedListComparitor("[[6]]")
lines.append(marker_2)
lines.append(marker_6)
lines = sorted(lines)
print((lines.index(marker_2) + 1) * (lines.index(marker_6) + 1))

