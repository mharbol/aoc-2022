
with open("day_07_input.txt") as file:
    lines = [line.strip() for line in file]

# remove the first entry ("$ cd /"), that will be the root node
del lines[0]

VERBOSE = False

class FileTreeNode:
    def __init__(self, name : str, size : int, parent) -> None:
        self.name = name
        self.size = size
        self.parent = parent
        self.children = dict()
    
    def __str__(self) -> str:
        return self.get_name()
    
    def get_name(self) -> str:
        return self.name
    
    def get_parent(self):
        return self.parent
    
    def get_dir(self, dir_name : str):
        return self.children[dir_name]
    
    def is_file(self) -> bool:
        return self.size != 0
    
    def is_dir(self) -> bool:
        return self.size == 0
    
    def get_child_dirs(self) -> list:
        return [node for node in self.get_children() if node.is_dir()]
    
    def get_children(self) -> list:
        return list(self.children.values())
    
    def add_node(self, node) -> None:
        if node.get_name() not in self.children.keys():
            self.children[node.get_name()] = node
        else:
            raise Exception()
    
    def get_size(self) -> int:
        if self.is_file():
            return self.size
        else:
            return sum(node.get_size() for node in self.get_children())
    
    def get_conditional_size(self, max_size : int) -> int:
        if self.is_file():
            return 0
        else:
            sz = self.get_size()
            return 0 if sz > max_size else sz
    
    def walk_nodes(self):
        # yield from all children
        for child in self.get_children():
            yield from child.walk_nodes()
        yield self

def new_dir(name : str, parent : FileTreeNode) -> FileTreeNode:
    return FileTreeNode(name, 0, parent)

def new_file(name : str, size : int) -> FileTreeNode:
    return FileTreeNode(name, size, None)

root = FileTreeNode("/", 0, None)
currentNode = root

def add_dir(name : str, node_ptr : FileTreeNode) -> FileTreeNode:
    node_ptr.add_node(new_dir(name, node_ptr))
    return node_ptr

def add_file(name : str, size : int, node_ptr : FileTreeNode) -> FileTreeNode:
    node_ptr.add_node(new_file(name, size))
    return node_ptr

def change_directory(name : str, node_ptr : FileTreeNode) -> FileTreeNode:
    if name == "..":
        return node_ptr.get_parent()
    else:
        return node_ptr.get_dir(name)

def process_line(line : str, node_ptr : FileTreeNode) -> FileTreeNode:
    if VERBOSE:
        print(line)
        print(f"Current dir: {node_ptr} -> {node_ptr.get_parent()}")
    command = line.split(" ")
    
    if command[0] == "$" and command[1] == "ls":
        return node_ptr
    elif command[0] == "$" and command[1] == "cd":
        return change_directory(command[2], node_ptr)
    elif command[0] == "dir":
        return add_dir(command[1], node_ptr)
    else:
        return add_file(command[1], int(command[0]), node_ptr)

for line in lines:
    currentNode = process_line(line, currentNode)
    if VERBOSE: print()

print(f"Total size   - {root.get_size()}")
unused_space = 70000000 - root.get_size()
print(f"Unused space - {unused_space}")
needed_space = 30000000 - unused_space
print(f"Needed space  - {needed_space}")

print(f"Conditional size - {sum(node.get_conditional_size(100_000) for node in root.walk_nodes())}")

all_dirs = []
for node in root.walk_nodes():
    if node.is_dir():
        all_dirs.append(node)

viable_nodes = filter(lambda node : node.get_size() >= needed_space, all_dirs)

ordered_nodes = sorted(map(lambda node : (node.get_size(), node.get_name()), viable_nodes))
print(ordered_nodes)