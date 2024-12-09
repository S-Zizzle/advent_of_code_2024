with open('2_input.txt', 'r') as file:
    part_one_count = 0

    for line in file:
        nums = list(map(int, line.split()))

        difs = []

        # Calculate the differences
        for i in range(len(nums) - 1):
            difs.append(nums[i] - nums[i+1])
        
        # make sure the difs are all the same polarity (nums increasing or decreasing)
        if not (all(x >= 0 for x in difs) or all(x <= 0 for x in difs)):
            continue
            
        # make sure they're all either 1, 2, or 3
        difs = [abs(x) for x in difs] #first get absoluate value

        if all(x in {1, 2, 3} for x in difs):
            part_one_count += 1
        
    
    print(f"Part one: {part_one_count}")