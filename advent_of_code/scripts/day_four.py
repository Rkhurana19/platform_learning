with open("../inputs/day_four_input.txt", "r") as file:
    overlaps = 0

    for line in file:
        intervals = line.strip().split(",")
        intervals[0] = list(map(int, intervals[0].split("-")))
        intervals[1] = list(map(int, intervals[1].split("-")))
        intervals.sort(key = lambda x : x[0])

        if intervals[0][1] >= intervals[1][0]:
            overlaps += 1
        
        print(intervals)
    
    print("Number of overlaps: " + str(overlaps))