# A means opponent plays rock
# B means opponent plays paper
# C means opponent plays scissors

# X means you need to lose
# Y means you need to draw
# Z means you need to win

points = {("A", "X") : 3,
		  ("A", "Y") : 4,
		  ("A", "Z") : 8,
		  ("B", "X") : 1,
		  ("B", "Y") : 5,
		  ("B", "Z") : 9,
		  ("C", "X") : 2,
		  ("C", "Y") : 6,
		  ("C", "Z") : 7}

with open("../inputs/day_two_input.txt", "r") as file:
	total_score = 0

	for line in file:
		move_pair = tuple(line.split())
		total_score += points[move_pair]

	print("Total score: " + str(total_score))
		
		

