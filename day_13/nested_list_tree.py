
# This is in its own file so it can reside in a place of glory away from whatever dirty
# code I may write to use it.

class NestedListComparitor:
    """
    Represents a node in a tree. Each node is either a terminal value (int or None) or another
    NestedListComparitor node. Overrides the lt, gt, and eq methods to compare them.
    I know that in the scope of the problem (part 1) this is overkill but it makes me feel
    like a real programmer.
    """

    def __init__(self, arg_str : str) -> None:
        """
        Makes a new node based on the input `str`. Will make `int` value as the value if
        the input is a singular int, otherwise will make a `list` of `NestedListComparitor`
        nodes to make it happen.

        A node which is an `int` or `None` (empty list) is a terminal node, otherwise value
        contains a `list` of nodes.

        Constructor assumes the input is a "complete nested list" meaning that the open
        brackets have corresponding closing brackets with no excess on either end. And
        that all whitespace characters have been removed (already done in the problem).
        """
        self.value : list[NestedListComparitor] | int = []

        # If the arg_str is "[]" we are good
        if arg_str == "[]":
            return

        # If the input is just an int then the value is an int then that is the value
        try:
            test_int = int(arg_str)
            end_index : int = 0
            self.value = test_int
            return
        except ValueError:
            pass

        # Now we know our entry is some type of populated list, remove the outermost brackets
        our_str : str = arg_str[1 : len(arg_str) - 1]
        self.value = []

        # use start_index to find the next value (int or another list)
        start_index : int = 0
        end_index : int = 0

        while start_index < len(our_str):

            new_node : NestedListComparitor = None

            # Check if we are starting a new list
            if our_str[start_index] == "[":

                # since it is a new list, make the next entry a NestedListComparitor for that list
                end_index = find_corresponding_bracket_outer_index(our_str, start_index)
                new_node = NestedListComparitor(our_str[start_index : end_index])

            # otherwise our value is an int
            else:
                # Find the index ending the current value
                try:
                    end_index = our_str.index(",", start_index)
                except ValueError:
                    # this means that we are at the end of our_str
                    end_index = len(our_str)

                new_node = NestedListComparitor(our_str[start_index : end_index])

            # checks if our parsing was successful
            if new_node is None:
                raise Exception(f"new_node is None for substring of {our_str} which is {our_str[start_index:]}")

            # append the new value and update our starting index
            self.value.append(new_node)
            start_index = end_index + 1


    def __lt__(self, other : object) -> bool:
        """
        Uses the rules specified by [Day 13](https://adventofcode.com/2022/day/13) to determine if
        self (left) is less than other (right).

        If both entries are `int` then we compare them. If left < right, return `True`. If left > right
        return `False`. If they are equal, move on.

        If both entries are `list` (in our datastructure that is a `NestedListComparitor`) we compare
        their individual entries. If a side runs out of items during comparison loop, that side
        is considered less than the other.

        If one side is an `int` we treat it as a single entry list and compare.
        """
        if type(other) != NestedListComparitor:
            raise Exception(f"Type {type(other)} cannot be compared to {type(self)}")

        # get the max size of the two NestedListComparitors, this will be the size we loop
        # over and use as a tiebreaker

        # if only one is empty list:
        if len(self) == 0 and len(other) > 0:
            return True
        if len(other) == 0 and len(self) > 0:
            return False
        max_len = max(len(self), len(other))
        # loop over both
        for index in range(max_len):

            # first check, one is out of bounds
            # if left can't keep going but right can. Left is less
            if len(self) <= index and len(other) > index:
                return True
            # if right can't keep going but left can, left is greater
            if len(other) <= index and len(self) > index:
                return False

            # go through the paces:
            # dealing with a len == 1 for each
            if len(self) == 1 and len(other) == 1:

                # if they are both ints
                if type(self.value) == int and type(other.value) == int:
                    if self.value == other.value:
                        continue
                    else:
                        return self.value < other.value

                # if they are both lists
                if type(self.value) == list and type(other.value) == list:

                    if self.value[0] == other.value[0]:
                        continue
                    else:
                        return self.value[0] < other.value[0]

                # if left is an int and right is a list
                if type(self.value) == int and type(other.value) == list:
                    if NestedListComparitor(self.value) == other.value[0]:
                        continue
                    else:
                        return NestedListComparitor(self.value) < other.value[0]

                # if left is list and right is int
                if type(self.value) == list and type(other.value) == int:
                    if NestedListComparitor(other.value) == self.value[0]:
                        continue
                    else:
                        return self.value[0] < NestedListComparitor(other.value)

            # at least one is a list
            else:

                # if left is an int and right is a list
                if type(self.value) == int and type(other.value) == list:
                    if NestedListComparitor(self.value) == other.value[0]:
                        continue
                    else:
                        return NestedListComparitor(self.value) < other.value[0]

                # if left is list and right is int
                if type(self.value) == list and type(other.value) == int:
                    if NestedListComparitor(other.value) == self.value[0]:
                        continue
                    else:
                        return self.value[0] < NestedListComparitor(other.value)

                if self.value[index] == other.value[index]:
                    continue
                else:
                    return self.value[index] < other.value[index]

        raise Exception("Exited method")

    def __gt__(self, other : object) -> bool:
        """
        Uses the `__lt__` and `__eq__` methods to compare `NestedListComparitor` objects.
        """
        if type(other) != NestedListComparitor:
            raise Exception(f"Type {type(other)} cannot be compared to {type(self)}")
        return self != other and other < self

    def __eq__(self, other: object) -> bool:
        """
        Check for equality by recursively checking each node.
        """
        if other is None:
            return False
        if type(other) != NestedListComparitor:
            raise Exception(f"Type {type(other)} cannot be compared to {type(self)}")

        # base comparison:
        # if both are ints, compare
        if type(self.value) == int and type(other.value) == int:
            return self.value == other.value

        # If both values are lists:
        if type(self.value) == list and type(other.value) == list:
            # if they are of differnent lengths, return False
            if len(self.value) != len(other.value):
                return False

            # loop through them both and see if they are the same
            for left, right in zip(self.value, other.value):
                if left != right:
                    return False
            return True

        # compare int to list
        if type(self.value) == int and type(other.value) == list:
            if len(other.value) != 1:
                return False

            return other.value[0] == self

        # compare list to int
        if type(self.value) == list and type(other.value) == int:
            if len(self.value) != 1:
                return False

            return self.value[0] == other

        raise Exception(f"Missing case in equals for {self.value} {type(self.value)} and \
                {other.value} {type(other.value)}")

    def __ne__(self, other: object) -> bool:
        """
        Uses `not __eq__` to check for inequality.
        """
        return not self == other

    def __len__(self) -> int:
        """
        The length of a node as number of child nodes. If the value is an `int` then `len` is 1.
        """
        return 1 if type(self.value) == int else len(self.value)

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        # terminal nodes
        if type(self.value) == int:
            return str(self.value)

        # Dealing with a list of nodes
        else:
            out = "["
            for node in self.value:
                out += str(node) + " "
            return out.strip() + "]"

def find_corresponding_bracket_outer_index(input_str : str, start_index : int) -> int:
    """
    Determines the `index + 1` of the corresponding close bracket (`]`) for the open bracket at the
    given `start_index`.
    """
    open_count = 0
    for index in range(start_index, len(input_str)):
        if input_str[index] == "[":
            open_count += 1
        elif input_str[index] == "]":
            open_count -= 1
        if open_count == 0:
            return index + 1
    raise Exception(f"Could not find closing bracket for {input_str} starting at {start_index}")

