with open("../inputs/day_nine_input.txt", "r") as file:
    num_knots = 10
    knots = [[0, 0] for _ in range(num_knots)]

    visited = set()
    visited.add(tuple(knots[num_knots - 1]))

    for line in file:
        direction, steps = line.split()
        steps = int(steps)

        while steps != 0:
            if direction == "U":
                knots[0][1] += 1
            elif direction == "D":
                knots[0][1] -= 1
            elif direction == "R":
                knots[0][0] += 1
            elif direction == "L":
                knots[0][0] -= 1

            for position in range(num_knots - 1):
                dx = knots[position][0] - knots[position + 1][0]
                dy = knots[position][1] - knots[position + 1][1]

                if abs(dx) == 2 and abs(dy) == 2:
                    knots[position + 1][0] += 1 if dx > 0 else -1
                    knots[position + 1][1] += 1 if dy > 0 else -1
                elif abs(dx) == 2:
                    knots[position + 1][0] += 1 if dx > 0 else -1
                    knots[position + 1][1] = knots[position][1]
                elif abs(dy) == 2:
                    knots[position + 1][0] = knots[position][0]
                    knots[position + 1][1] += 1 if dy > 0 else -1
                
            visited.add(tuple(knots[num_knots - 1]))
            steps -= 1

    print("Number of unique positions: " + str(len(visited)))