grid = []

with open('6_input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.strip('\n')))

i, j = [(i, j) for i, row in enumerate(grid) for j, char in enumerate(row) if char in ['^', '>', 'v', '<']][0]

finished = False

while not finished:
    char = grid[i][j]
    next = ''
    try:
        if char == '^':
            next = grid[i-1][j]
        elif char == '>':
            next = grid[i][j+1]
        elif char == 'v':
            next = grid[i+1][j]
        elif char == '<':
            next = grid[i][j-1]
    except IndexError:
        grid[i][j] = 'X'
        finished = True
        continue
    
    if next == '#':
        if char == '^':
            grid[i][j] = '>'
        elif char == '>':
            grid[i][j] = 'v'
        elif char == 'v':
            grid[i][j] = '<'
        elif char == '<':
            grid[i][j] = '^'
        
        continue

    grid[i][j] = 'X'

    if char == '^':
        grid[i-1][j] = '^'
        i -= 1
    elif char == '>':
        grid[i][j+1] = '>'
        j += 1
    elif char == 'v':
        grid[i+1][j] = 'v'
        i += 1
    elif char == '<':
        grid[i][j-1] = '<'
        j -= 1

p1_count = 0

for row in grid:
    p1_count += row.count('X')

print(f"Part one count: {p1_count}")

obstacles = []

for irow, row in enumerate(grid):
    for icol, char in enumerate(row):
        if char == '#':
            obstacles.append((irow, icol))

for (i, j) in obstacles:
    for a in [-1, 1]:
        pass