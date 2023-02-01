
# just get the lines as a list and we'll deal with it.
# this is the quick and dirty python solution
with open("day_03_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

# use the ascii value of the characters to assign the priority.
# This is annoying that lower case is before upper case
def priority(letter : str) -> int:

    num = ord(letter)

    if num in range(ord('a'), ord('z') + 1):
        return num - ord('a') + 1

    return num - ord('A') + 27

# nested for loop for some sweet n^2 action
def mutual_item(left, right) -> str:
    for letter in left:
        if letter in right:
            return letter

# could have made this one function but making it one logical leap at a time
# use int division and list slice to feed mutual_item()
def find_mutual_letter(s : str) -> str:
    return mutual_item(s[:len(s) // 2], s[len(s) // 2:])

# love getting to use map() and filter() and reduce()
# applies the function to every item in the iterable and returns a new
# iterable with the results.
# This way can chain together finding the mutual letter, then feed that to priority()
# and finally sum it all together


mut_letters = map(find_mutual_letter, lines)
priorities = map(priority, mut_letters)
print(sum(priorities))

# I am not proud of this one.
# Effectively doing the nested for loop to find all common letters between
# l0 and l1. Then looping over that (inter) to see which one is common with l2
def mut_letter_3(l0, l1, l2) -> str:
    inter = []
    for ln_1 in l0:
        if ln_1 in l1:
            inter.append(ln_1)
    for ln_2 in inter:
        if ln_2 in l2:
            return ln_2


total = 0
for i in range(0, len(lines), step=3):
    sl = lines[i : i + 3]
    total += priority(mut_letter_3(sl[0], sl[1], sl[2]))

print(total)

