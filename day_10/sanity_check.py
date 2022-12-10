
with open("day_10_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

class Freq:
    def __init__(self):
        self.val = 1
        self.cycle = 0
        self.doing = 0
        self.record = []
    
    # this is a doozy of a method:
    def process(self, value):
        # at the start of each line, start a cycle
        self.cycle += 1
        # add mid-cycle state to the record
        self.record.append((self.cycle, self.val))
        # set the in-progress state to th input
        self.doing = value
        # if the in-progress is an operation, process the new operation
        if self.doing != 0:
            # start another cycle...
            self.cycle += 1
            # updoot the record...
            self.record.append((self.cycle, self.val))
            # do the same cycle thing
            self.val += self.doing
            # clear out the process queue
            self.doing = 0 
        

def make_input(lines):
    out = []
    for line in lines:
        if line == 'noop':
            out.append(0)
        else:
            out.append(int(line.split(" ")[1]))
    return out

freq = Freq()

input = make_input(lines)

for i in input:
    freq.process(i)

# add up the lot
tot = 0
for pairs in freq.record:
    if pairs[0] in [20, 60, 100, 140, 180, 220]:
        tot += pairs[0] * pairs[1]

print(tot)

# make a 6 row by 40 column array of bools
display = []
for row in range(6):
    n = []
    for x in range(40):
        n.append(False)
    display.append(n)

# function that alters the display based on cycle and value
def alter_display(cycle, value, display):

    # the row inc every 40 cycles
    row = cycle // 40

    # column is offset left by one and tied to the row, so use mod to get col position regarless of row
    column = (cycle - 1) % 40

    # if column in sprite range:
    if column == value - 1 or column == value or column == value + 1:
        display[row][column] = True

for rec in freq.record:
    alter_display(rec[0], rec[1], display)

# pretty-prints the bool arr
def show_disp(display):
    for row in display:
        for col in row:
            print('#' if col else ".", end = "")
        print()

show_disp(display)