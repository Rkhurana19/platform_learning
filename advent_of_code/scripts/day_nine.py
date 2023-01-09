# data structures:
# 1. set to store visited locations of the tail node

# continuously update head position by parsing input step by step
# update tail position based on the following rules:
# 1. calculate dx as follows: head_x - tail_x
# 2. calculate dy as follows: head_y - tail_y
# 3. cases to consider: either |dx| equals 2 or |dy| equals 2
#    a. case 1: |dx| = 2
#       i. example 1: tail - (0, 0), head - (2, 0), dx = 2. move tail to (1, 0)
#       ii. example 2: tail - (2, 0), head - (0, 0), dx = -2. move tail to (1, 0)
#       iii. example 3: tail - (2, 2), head - (4, 3), dx = 2. move tail to (3, 3)
#       iv. example 4: tail - (4, 3), head - (2, 2), dx = -2. move tail to (3, 2)
#    b. case 2: |dy| = 2. same insights as above, adjust y pos based on sign, keep x coordinate same as head.

with open("../inputs/day_nine_input.txt", "r") as file:
    head = [0, 0]
    tail = [0, 0]

    visited = set()
    visited.add(tuple(tail))

    for line in file:
        direction, steps = line.split()
        steps = int(steps)

        while steps != 0:
            if direction == "U":
                head[1] += 1
            elif direction == "D":
                head[1] -= 1
            elif direction == "R":
                head[0] += 1
            elif direction == "L":
                head[0] -= 1

            dx = head[0] - tail[0]
            dy = head[1] - tail[1]

            if abs(dx) == 2:
                tail[0] += 1 if dx > 0 else -1
                tail[1] = head[1]
            elif abs(dy) == 2:
                tail[0] = head[0]
                tail[1] += 1 if dy > 0 else -1

            visited.add(tuple(tail))
            steps -= 1

    print("Number of unique positions: " + str(len(visited)))