def grouper(iterable, n, fill = None):
    args = [iter(iterable)] * n
    return zip(*args)


with open("../inputs/day_three_input.txt", "r") as file:
    priority = 0

    for elf_one, elf_two, elf_three in grouper(file, 3):
        elf_one = str(elf_one).strip()
        elf_two = str(elf_two).strip()
        elf_three = str(elf_three).strip()

        badge = "".join(set(elf_one).intersection(set(elf_two), set(elf_three)))

        if badge.isupper():
            priority += ord(badge) - ord("A") + 27
        else:
            priority += ord(badge) - ord("a") + 1
    
    print("Cumulative priority: " + str(priority))