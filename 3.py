import re

with open('3_input.txt', 'r') as file:
    p1_strs = []
    p2_strs = []
    for line in file:
        p1_strs += re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)", line)
        p2_strs += re.findall("mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)", line)
    
    p1_total = 0
    p2_total = 0

    for mul in p1_strs:
        nums = re.findall("[0-9]{1,3}", mul)
        p1_total += int(nums[0]) * int(nums[1])
    
    using = True
    for x in p2_strs:
        if x == "don't()":
            using = False
            continue

        if x == "do()":
            using = True
            continue

        if not using:
            continue

        nums = re.findall("[0-9]{1,3}", x)
        p2_total += int(nums[0]) * int(nums[1])


    
    print(f"Part one total: {p1_total}")
    print(f"Part two total: {p2_total}")