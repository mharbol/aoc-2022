
from enum import Enum

with open("day_14_input.txt") as file:
    real_input = [line.strip() for line in file.readlines()]

test_input = [
    "498,4 -> 498,6 -> 496,6",
    "503,4 -> 502,4 -> 502,9 -> 494,9"
]

# Stands in for the objects making up the cave
class PlatformToken(Enum):
    AIR = 0
    ROCK = 1
    SAND = 2

    def __str__(self) -> str:
        if self.value == PlatformToken.AIR:
            return " "
        elif self.value == PlatformToken.ROCK:
            return "#"
        elif self.value == PlatformToken.SAND:
            return "o"

    def __repr__(self) -> str:
        return str(self)

# turns the arrow mass of points into a list of verticies for
# "platform" style rock formations
def parse_line(line : str) -> list[tuple(int, int)]:
    pass

def get_min_max_x_y(input_arr : list[list[tuple(int, int)]]) -> tuple(int, int, int, int):
    pass

def adjust_lines(lines : list[tuple(int, int)], min_x : int, max_x : int,
                    min_y : int, max_y : int) -> list[tuple(int, int)]:
    pass
