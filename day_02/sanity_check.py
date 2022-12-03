
# rock paper scissors constants
ROCK = 1
PAPER = 2
SCISSORS = 3

WIN = 6
LOSS = 0
DRAW = 3

# will be used for comparison. If the opponent is equivalent to the
# value to the left (wrapped around), then it is a win.
# the token's index is one less than its value
WIN_CIRCLE = [ROCK, PAPER, SCISSORS]

# returns the victory score of the right side player
def elf_rps(left : int, right : int) -> int:

    # DRAW case
    if left == right:
        return right + DRAW

    if  WIN_CIRCLE[(right + 1) % 3] == left: # the value plus 1 (mod 3) is the same as the value 1 to the left
        return WIN + right
    return LOSS + right

def elf_rps_actual(opponent_move : int, outcome : int) -> int:
    if outcome == DRAW:
        return DRAW + opponent_move
    
    if outcome == LOSS:
        return WIN_CIRCLE[(opponent_move + 1) % 3] # same as before but now it is me that will have the losing value
    return WIN_CIRCLE[opponent_move % 3] + WIN # this is one move to the right, a winning value

letter_to_outcome = {
    "A" : ROCK,
    "B" : PAPER,
    "C" : SCISSORS,
    "X" : LOSS,
    "Y" : DRAW,
    "Z" : WIN, 
}

def elf_rps_actual_str(line : str):
    return elf_rps_actual(letter_to_outcome[line[0]], letter_to_outcome[line[2]])

letter_to_move = {
    "A" : ROCK,
    "B" : PAPER,
    "C" : SCISSORS,
    "X" : ROCK,
    "Y" : PAPER,
    "Z" : SCISSORS,
}

def elf_rps_str(line : str) -> int:
    return elf_rps(letter_to_move[line[0]], letter_to_move[line[2]])


with open("day_02_input.txt") as text_doc:
    lines = text_doc.readlines()

acc1 = 0
acc2 = 0
for line in lines:
    acc1 += elf_rps_str(line)
    acc2 += elf_rps_actual_str(line)

print(f"Total score: {acc1}")
print(f"Total score with updated rules: {acc2}")
