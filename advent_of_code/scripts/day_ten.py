with open("../inputs/day_ten_input.txt", "r") as file:
    cycle = 0
    register = 1
    signal_strength = 0

    for instruction in file:
        instruction = instruction.split()

        cycle += 1
        if (cycle - 20) % 40 == 0:
            signal_strength += register * cycle
        
        if instruction[0] == "addx":
            cycle += 1
            if (cycle - 20) % 40 == 0:
                signal_strength += register * cycle
                
            register += int(instruction[1])

    print("Sum of signal strengths: " + str(signal_strength))