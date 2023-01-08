forest = []

with open("../inputs/day_eight_input.txt", "r") as file:
    row = []

    while byte := file.read(1):
        if byte == "\n":
            forest.append(row)
            row = []
        else:
            row.append(int(byte))
    
    if row != []:
        forest.append(row)

num_rows = len(forest)
num_cols = len(forest[0])
visibility = [[0] * num_cols for _ in range(num_rows)]

for row in range(num_rows):
    left_max = -1
    right_max = -1

    for col in range(num_cols):
        if forest[row][col] > left_max:
            visibility[row][col] = 1
            left_max = forest[row][col]
    
    for col in range(num_cols, 0, -1):
        if forest[row][col - 1] > right_max:
            visibility[row][col - 1] = 1
            right_max = forest[row][col - 1]

for col in range(num_cols):
    top_max = -1
    bottom_max = -1

    for row in range(num_rows):
        if forest[row][col] > top_max:
            visibility[row][col] = 1
            top_max = forest[row][col]
    
    for row in range(num_rows, 0, -1):
        if forest[row - 1][col] > bottom_max:
            visibility[row - 1][col] = 1
            bottom_max = forest[row - 1][col]
    
visible_trees = sum([sum(row) for row in visibility])
print("Visible trees: " + str(visible_trees))