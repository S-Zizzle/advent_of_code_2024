problems = {}

with open('7_input.txt', 'r') as file:
    for line in file:
        line = line.split(':')
        # THIS ASSUMES THERE IS ONLY EVER 1 OF EACH ANSWER.....
        if line[0] in problems: print("UH OH!!!!!!!!!!!!!!!!!!!!!", line[0])
        problems[line[0]] = list(line[1].strip('\n').strip().split(' '))

for answer, numbers in problems.items():
    # add + between every number
    nums = []
    for i in range(len(numbers)):
        nums.append(numbers[i])
        if i < len(numbers) - 1:
            nums.append('+')
    
    # try every combination of changing + for * until we find answer or end up with no +
    for i in range(1, len(nums)-1, 2):
        #calculate and see if good, of yes the add answer to counter and continue parent loop
        
        #not good
        # if no + in list then continue big loop

        # change value at ith position to *
        pass