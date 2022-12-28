import re

with open("../inputs/day_five_input.txt", "r") as file:
    primer = file.readline().rstrip("\n")
    num_stacks = (len(primer) + 1) // 4
    stacks = [[] for _ in range(num_stacks)]

    while primer != "":
        for position in range(0, len(primer), 4):
            item = primer[position : position + 3][1]
            if item.isalpha():
                stacks[position // 4].append(item)

        primer = file.readline().rstrip("\n")
    
    stacks = [stack[::-1] for stack in stacks]

    for line in file:
        operation = list(map(int, re.findall(r"\d+", line)))

        items = stacks[operation[1] - 1][-operation[0]:]
        del stacks[operation[1] - 1][-operation[0]:]
  
        stacks[operation[2] - 1].extend(items)

    print("Top-most items of each stack: ")
    for stack in stacks:
        print(stack[-1], end = "")