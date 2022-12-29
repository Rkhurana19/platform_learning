class Node:
    def __init__(self, parent = None):
        self.directories = {".." : parent}
        self.files = []
        self.size = None
    
    def add_file(self, size, name):
        self.files.append((size, name))
    
    def add_directory(self, name):
        self.directories[name] = Node(self)
    
root_node = Node()

with open("../inputs/day_seven_input.txt", "r") as file:
    current_node = root_node
    
    for line in file:
        line = line.split()

        if line[0] == "$" and line[1] == "cd":
            current_node = (root_node if line[2] == "/" 
                else current_node.directories[line[2]])
        elif line[0] != "$":
            (current_node.add_directory(line[1]) if line[0] == "dir"
                else current_node.add_file(int(line[0]), line[1]))

def compute_sizes(node):
    node.size = sum([size for size, _ in node.files])

    for name, child in node.directories.items():
        if name != "..":
            compute_sizes(child)
            node.size += child.size

def identify_candidate(node, space_needed):
    candidate_size = node.size

    for name, child in node.directories.items():
        if name != ".." and child.size >= space_needed:
            candidate_size = min(candidate_size, identify_candidate(child, space_needed))

    return candidate_size

compute_sizes(root_node)

total_disk_space = 70000000
needed_disk_space = 30000000
unused_space = total_disk_space - root_node.size
space_needed = needed_disk_space - unused_space

print("Deleted directory size: " + str(identify_candidate(root_node, space_needed)))