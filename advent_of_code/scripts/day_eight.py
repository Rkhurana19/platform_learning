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

visibility = [[1] * num_cols for _ in range(num_rows)]

for row in range(num_rows):
    monotone_stack = [0]

    for col in range(1, num_cols):
        while (monotone_stack and forest[row][col] 
                >= forest[row][monotone_stack[-1]]):
            popped_index = monotone_stack.pop()
            visibility[row][popped_index] *= col - popped_index

        monotone_stack.append(col)
    
    while monotone_stack:
        popped_index = monotone_stack.pop()
        visibility[row][popped_index] *= num_cols - popped_index - 1
    
    monotone_stack = [num_cols - 1]

    for col in range(num_cols - 2, -1, -1):
        while (monotone_stack and forest[row][col] 
                >= forest[row][monotone_stack[-1]]):
            popped_index = monotone_stack.pop()
            visibility[row][popped_index] *= popped_index - col

        monotone_stack.append(col)
    
    while monotone_stack:
        popped_index = monotone_stack.pop()
        visibility[row][popped_index] *= popped_index

for col in range(num_cols):
    monotone_stack = [0]

    for row in range(1, num_rows):
        while (monotone_stack and forest[row][col]
                >= forest[monotone_stack[-1]][col]):
            popped_index = monotone_stack.pop()
            visibility[popped_index][col] *= row - popped_index
        
        monotone_stack.append(row)
    
    while monotone_stack:
        popped_index = monotone_stack.pop()
        visibility[popped_index][col] *= num_rows - popped_index - 1

    monotone_stack = [num_rows - 1]

    for row in range(num_rows - 2, -1, -1):
        while (monotone_stack and forest[row][col]
                >= forest[monotone_stack[-1]][col]):
            popped_index = monotone_stack.pop()
            visibility[popped_index][col] *= popped_index - row

        monotone_stack.append(row)
    
    while monotone_stack:
        popped_index = monotone_stack.pop()
        visibility[popped_index][col] *= popped_index

max_scenic_score = max([max(row) for row in visibility])
print("Max scenic score: " + str(max_scenic_score))