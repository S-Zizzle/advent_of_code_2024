grid = []

with open('16_input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.strip('\n')))

s_y = s_x = e_y = e_x = 0

for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char == 'S':
            s_y, s_x = i, j
        elif char == 'E':
            e_y, e_x = i, j

