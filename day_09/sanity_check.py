
with open("day_09_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]


class Segment:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    # This determines if the segment needs to move or can just chill where it is
    def is_one_away_from(self, head):
        if abs(self.x - head.x) > 1:
            return False
        if abs(self.y - head.y) > 1:
            return False
        return True

    def make_move(self, move : str):
        if move == 'U':
            self.move_up()
        if move == 'D':
            self.move_down()
        if move == 'R':
            self.move_right()
        if move == 'L':
            self.move_left()

    # Definitely a better way to pick moves, this is just easy and bullet-proof
    # Returns the postition as a tuple so we can track unique spots the tail Segment has been
    def move_to_cover(self, head):
        # no move needed
        if self.is_one_away_from(head):
            return (self.x, self.y)

        # up
        if head.x == self.x and head.y == self.y + 2:
            self.move_up()
            return (self.x, self.y)

        # down
        if head.x == self.x and head.y == self.y - 2:
            self.move_down()
            return (self.x, self.y)

        # right
        if head.y == self.y and head.x == self.x + 2:
            self.move_right()
            return (self.x, self.y)
        # left
        if head.y == self.y and head.x == self.x - 2:
            self.move_left()
            return (self.x, self.y)

        # up and right
        if (head.x == self.x + 1 and head.y == self.y + 2) or (head.x == self.x + 2 and head.y == self.y + 1) or (head.x == self.x + 2 and head.y == self.y + 2):
            self.move_right()
            self.move_up()
            return (self.x, self.y)

        # up and left
        if (head.x == self.x - 1 and head.y == self.y + 2) or (head.x == self.x - 2 and head.y == self.y + 1) or (head.x == self.x - 2 and head.y == self.y + 2):
            self.move_left()
            self.move_up()
            return (self.x, self.y)

        # down and right
        if (head.x == self.x + 2 and head.y == self.y - 1) or (head.x == self.x + 1 and head.y == self.y - 2) or (head.x == self.x + 2 and head.y == self.y - 2):
            self.move_right()
            self.move_down()
            return (self.x, self.y)

        # down and left
        if (head.x == self.x - 2 and head.y == self.y - 1) or (head.x == self.x - 1 and head.y == self.y - 2) or (head.x == self.x - 2 and head.y == self.y - 2):
            self.move_left()
            self.move_down()
            return (self.x, self.y)

        # Here as a way to show my moves aren't working
        raise Exception(f"Hx{head.x} Hy{head.y} Tx{self.x} Ty{self.y}")


# Part 1
test_input = ["R 4", "U 4", "L 3", "D 1", "R 4", "D 1", "L 5", "R 2"]

# turns the coded moves into individual ones
def move_maker(lines):
    out = []
    for line in lines:
        move = line.split(" ")
        for x in range(int(move[1])):
            out.append(move[0])
    return out


# keep track of past positions
past_positions = []

# starting positions
head = Segment(0, 0)
tail = Segment(0, 0)

moves = move_maker(lines)

for move in moves:
    head.make_move(move)
    past_positions.append(tail.move_to_cover(head))

print(len(set(past_positions)))

# Input for part 2
test_input = ["R 5", "U 8", "L 8", "D 3", "R 17", "D 10", "L 25", "U 20"]

moves = move_maker(lines)

# make a new segment per knot
seggs = [Segment(0, 0) for x in range(10)]
last_pos = set()
for move in moves:

    seggs[0].make_move(move)

    # can loop over 1-8 easily
    for x in range(1, 9):
        seggs[x].move_to_cover(seggs[x - 1])

    # just keep track of where 9 is
    last_pos.add(seggs[9].move_to_cover(seggs[8]))

    # show current position for each segment
    print(f"Move: {move}", end=" |  ")
    for x, seg in enumerate(seggs):
        print(f"{'H' if x == 0 else ('T' if x == 9 else x)}({seg.x} {seg.y})", end=" ")
    print()

print(len(last_pos))

