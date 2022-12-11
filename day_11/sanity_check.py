
with open("day_11_input.txt") as file:
    lines = [line.strip() for line in file.readlines()]

class Item:
    def __init__(self, value : int) -> None:
        self.value = value

    def update_worry(self, operation) -> None:
        self.value = operation(self.value)
    
    def reduce_worry(self):
        # self.value = self.value // 3
        pass
    
    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)
    

class Monkey:
    
    def __init__(self, index: int, worry_queue : list[Item], test_divisor : int, 
                 operation, true_toss : int, false_toss : int) -> None:
        self.index = index
        self.worry_queue = worry_queue
        self.test_divisor = test_divisor
        self.operation = operation
        self.true_toss = true_toss
        self.false_toss = false_toss
        self.item_inspection_count = 0
    
    def __repr__(self):
        return str(self)
    
    def __str__(self) -> str:
        return f"Monkey: {self.index} {self.worry_queue} Div by: {self.test_divisor} " \
             + f"{self.operation} True: toss to {self.true_toss} False toss to: {self.false_toss}"
    
    def inspect_next_item(self) -> tuple[int, Item]:
        # print(f"Monkey {self.index} {self.worry_queue}")
        item = self.worry_queue.pop(0) # next item

        # print(f"{item} -> ", end = "")
        item.update_worry(self.operation) # play with item
        # print(f"{item} -> ", end = "")

        item.reduce_worry() # reduce worry

        # print(f"{item}")
        to = self.throws_to(item) 
        # print(f"Throw to: {to}")
        self.item_inspection_count += 1

        # print(f"New count: {self.item_inspection_count}")
        return (to, item)
    
    def throws_to(self, item : Item) -> int:
        if item.value % self.test_divisor == 0:
            return self.true_toss
        else:
            return self.false_toss

    def has_next(self) -> bool:
        return len(self.worry_queue) > 0
    
    def append_item(self, item : Item) -> None:
        self.worry_queue.append(item)

monkeys = [
    Monkey(0, [Item(x) for x in [56, 56, 92, 65, 71, 61, 79]], 3, lambda x : x * 7, 3, 7),
    Monkey(1, [Item(x) for x in [61, 85]], 11, lambda x : x + 5, 6, 4),
    Monkey(2, [Item(x) for x in [54, 96, 82, 78, 69]], 7, lambda x : x * x, 0, 7),
    Monkey(3, [Item(x) for x in [57, 59, 65, 95]], 2, lambda x : x + 4, 5, 1),
    Monkey(4, [Item(x) for x in [62, 67, 80]], 19, lambda x : x * 17, 2, 6),
    Monkey(5, [Item(x) for x in [91]], 5, lambda x : x + 7, 1, 4),
    Monkey(6, [Item(x) for x in [79, 83, 64, 52, 77, 56, 63, 92]], 17, lambda x : x + 6, 2, 0),
    Monkey(7, [Item(x) for x in [50, 97, 76, 96, 80, 56]], 13, lambda x : x + 3, 3, 5)
]

print(monkeys)

for count in range(1000):
    print(f"Count: {count}")
    for monkey in monkeys:
        while monkey.has_next():
            throw_to, item = monkey.inspect_next_item()
            monkeys[throw_to].append_item(item)
        print(f"Monkey: {monkey.index} Inspections: {monkey.item_inspection_count}")

inspection_count = [monkey.item_inspection_count for monkey in monkeys]

print(inspection_count)

inspection_count = list(reversed(sorted(inspection_count)))

print(inspection_count)

print(inspection_count[0] * inspection_count[1])