grid = []
movements = []

with open('15_input.txt', 'r') as file:
    movements_flag = False
    for line in file:
        if line == '\n':
            movements_flag = True
            continue
        
        if movements_flag:
            movements.extend(list(line.strip('\n')))
        else:
            line = grid.append(list(line.strip('\n')))


bot_y, bot_x = [(i, j) for i, row in enumerate(grid) for j, char in enumerate(row) if char == '@'][0]

for movement in movements:
    mv = (0,0)
    if movement == '^': mv = (-1, 0)
    elif movement == '>': mv = (0, 1)
    elif movement == 'v': mv = (1, 0)
    elif movement == '<': mv = (0, -1)

    ty, tx = bot_y, bot_x
    searching = True
    moving = False
    while searching:
        next_tile = grid[ty+mv[0]][tx+mv[1]]

        if next_tile == '.':
            grid[bot_y][bot_x] = '.'
            grid[bot_y+mv[0]][bot_x+mv[1]] = '@'
            if moving:
                grid[ty+mv[0]][tx+mv[1]] = 'O'
            moving = False
            bot_y += mv[0]
            bot_x += mv[1]
            searching = False
        
        if next_tile == '#':
            searching = False
        
        if next_tile == 'O':
            moving = True
            ty += mv[0]
            tx += mv[1]
    
    '''for row in grid:
        print(''.join(row))
    
    pass'''

total = 0

for i, row in enumerate(grid):
    for j, char in enumerate(row):
        if char == 'O':
            total += (i*100) + j

print(total)