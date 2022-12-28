with open("../inputs/day_one_input.txt", "r") as file:
	calories = []
	current_elf = 0

	for line in file:
		if line.strip() != "":
			current_elf += int(line.strip())
		else:
			calories.append(current_elf)
			current_elf = 0

	calories.sort(reverse = True)
	print("Calories: " + str(sum(calories[0:3])))