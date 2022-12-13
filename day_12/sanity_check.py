with open("day_12_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

test_input = [
    "Sabqponm", 
    "abcryxxl", 
    "accszExk", 
    "acctuvwj", 
    "abdefghi"
]

array = lines

# Makes a bool array array to represent if a node has been visited before
def make_been_visited(arr : list[str]) -> list[list[bool]]:
    out = []
    for line in arr:
        out.append([False for letter in line])
    return out


def can_step(from_letter : str, to_letter : str) -> bool:
    
    from_val = ord(from_letter)
    if from_letter == 'S':
        from_val = ord('a')
    to_val = ord(to_letter)
    if to_letter == 'E':
        to_val = ord('z')
    
    return to_val <= from_val + 1

class Position:
    def __init__(self, row : int, col : int, count : int) -> None:
        self.row = row
        self.col = col
        self.count = count
    
    def all_available_moves(self, arr : list, been_there, MAX_ROW, MAX_COL) -> list:
        out = []

        # North
        if self.row != 0 and (not been_there[self.row - 1][self.col]) and \
        can_step(arr[self.row][self.col], arr[self.row - 1][self.col]):
            out.append(Position(self.row - 1, self.col, self.count + 1))

        # South
        if self.row + 1 < MAX_ROW and (not been_there[self.row + 1][self.col]) \
            and can_step(arr[self.row][self.col], arr[self.row + 1][self.col]):
            out.append(Position(self.row + 1, self.col, self.count + 1))

        # East
        if self.col + 1 < MAX_COL and (not been_there[self.row][self.col + 1]) \
            and can_step(arr[self.row][self.col], arr[self.row][self.col + 1]):
            out.append(Position(self.row, self.col + 1, self.count + 1))

        # West
        if self.col != 0 and (not been_there[self.row][self.col - 1]) and \
            can_step(arr[self.row][self.col], arr[self.row][self.col - 1]):
            out.append(Position(self.row, self.col - 1, self.count + 1))

        return out


def trail_bfs(start_row, start_col, arr):

    start = Position(start_row, start_col, 0)

    been_there = make_been_visited(arr)

    # Time for the BFS, my nemesis:
    queue : list[Position] = []

    been_there[start_row][start_col] = True

    # Out of bounds numbers for row and column
    MAX_ROW = len(been_there)
    MAX_COL = len(been_there[0])

    queue.append(start)

    while len(queue) > 0:

        current = queue.pop(0)

        if array[current.row][current.col] == 'E':
            return current.count
        for next_item in current.all_available_moves(arr, been_there, MAX_ROW, MAX_COL):
            been_there[next_item.row][next_item.col] = True
            queue.append(next_item)
    return None

# loop over array and get all starting points
all_starting_points = []

for row in range(len(array)):
    for col in range(len(array[row])):
        if array[row][col] == 'a' or array[row][col] == 'S':
            all_starting_points.append((row, col))

print(all_starting_points)

all_path_len = []
# loop over and test all
for x in all_starting_points:
    row, col = x
    all_path_len.append(trail_bfs(row, col, array))

print(all_path_len)

all_path_len = filter(lambda x : x != None, all_path_len)
print(all_path_len)
print(min(all_path_len))