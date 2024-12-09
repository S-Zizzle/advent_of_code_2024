# Extract input data from file
col1 = []
col2 = []

with open('1_input.txt', 'r') as file:
    for line in file:
        num1, num2 = map(int, line.split())
        
        col1.append(num1)
        col2.append(num2)

# Part two (solve before sorting the lists)
occurence_map = {}
col1_distinct = list(set(col1))
for item in col1_distinct:
    occurence_map[item] = col2.count(item)

print(f"Part two answer: {sum(map(lambda x: x[0] * x[1], occurence_map.items()))}")


# Sort data asc
col1.sort()
col2.sort()

print(f"Part one answer: {sum(map(lambda x: abs(x[0] - x[1]), zip(col1, col2)))}")


