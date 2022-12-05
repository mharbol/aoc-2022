
with open("day_04_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

def contains(l0, r0, l1, r1) -> bool:
    return ((l0 <= l1) and (r0 >= r1)) or ((l1 <= l0) and (r1 >= r0))

def listify(line : str) -> list[str]:
    line = line.replace(",", " ").replace("-", " ")
    l = line.split(" ")
    l = [int(s) for s in l]
    return l

def solve(string : str) -> int:
    l = listify(string)
    return contains(l[0], l[1], l[2], l[3])

def overlap(string : str) -> int:
    l = listify(string)
    l0, r0, l1, r1 = l[0], l[1], l[2], l[3]
    return solve(string) or (l0 <= l1 and r0 >= l1 and r1 >= r0) or (l1 <= l0 and l0 <= r1 and r0 >= r1)

print("Crappy Way:")
print(sum(map(solve, lines)))
print(sum(map(overlap, lines)))

# much easier way with sets:
def envlop_set(lst):
    l = listify(lst)
    l0, r0, l1, r1 = l[0], l[1], l[2], l[3]
    left_set = set(range(l0, r0 + 1))
    right_set = set(range(l1, r1 + 1))
    return (left_set & right_set == right_set) or (left_set & right_set == left_set)

def overlap_set(lst):
    l = listify(lst)
    l0, r0, l1, r1 = l[0], l[1], l[2], l[3]
    left_set = set(range(l0, r0 + 1))
    right_set = set(range(l1, r1 + 1))
    return len(left_set & right_set) != 0

print("Set way:")
print(sum(map(envlop_set, lines)))
print(sum(map(overlap_set, lines)))