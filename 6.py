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

#for i in row
#for j in col
#have data of visited nodes
# run mainloop
# keep map of places we've been and direction facing
# if wwe've already been on this tile facing this direction then we are looping

''' This is trying to do the clever way. For now just brute force it
obstacles = []
p2_count = 0

for irow, row in enumerate(grid):
    for icol, char in enumerate(row):
        if char == '#':
            obstacles.append((irow, icol))

for ob1 in obstacles:
    for ob2 in obstacles:
        for ob3 in obstacles:
            if ob1 == ob2 or ob1 == ob3 or ob2 == ob3: continue

            #check if ob1, 2, 3 line up like the drawing. if they do then +1 to counter
'''