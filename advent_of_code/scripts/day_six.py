from collections import deque

with open("../inputs/day_six_input.txt", "r") as file:
    processed_characters = deque()
    current_marker = [0] * 26
    bytes_encountered = 0
    unique_characters = 0

    while byte := file.read(1):
        bytes_encountered += 1

        if bytes_encountered > 14:
            buffer = processed_characters.popleft()

            mapped_index = ord(buffer) - ord("a")
            current_marker[mapped_index] -= 1
            if current_marker[mapped_index] == 0:
                unique_characters -= 1
        
        mapped_index = ord(byte) - ord("a")
        if current_marker[mapped_index] == 0:
            unique_characters += 1
        current_marker[mapped_index] += 1

        processed_characters.append(byte)

        if unique_characters == 14:
            break

    print("Marker appears after the {} characters".format(bytes_encountered))
        
