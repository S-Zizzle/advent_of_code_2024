grid = []

with open('4_input.txt', 'r') as file:
    for line in file:
        grid.append(list(line))

search = [[-1, 0], #up
          [-1, 1], #upright
          [0, 1], #right
          [1, 1], #downright
          [1, 0], #down
          [1, -1], #downleft
          [0, -1], #left
          [-1, -1]] #upleft


## part one
p1_count = 0

for irow, row in enumerate(grid):
    for icol, char in enumerate(row):
        if char == 'X':
            for dir in search:
                def loopMas():
                    for i, nchar in enumerate('MAS'):
                        try:
                            x = irow + (dir[0] * (i+1))
                            y = icol + (dir[1] * (i+1))

                            if x < 0 or y < 0:
                                return 0

                            if grid[x][y] != nchar:
                                return 0
                        except IndexError:
                            return 0
                    return 1
                p1_count += loopMas()

print(f"Part one count: {p1_count}")

p2_count = 0

for irow, row in enumerate(grid):
    if irow == 0 or irow == len(grid)-1:
        continue

    for icol, char in enumerate(row):
        if icol == 0 or icol == len(row)-1:
            continue

        if char == 'A':
            back = grid[irow-1][icol-1] + grid[irow][icol] + grid[irow+1][icol+1] # \
            forward = grid[irow+1][icol-1] + grid[irow][icol] + grid[irow-1][icol+1] # /

            if ''.join(back) not in ['MAS', 'SAM']:
                continue
            
            if ''.join(forward) not in ['MAS', 'SAM']:
                continue

            p2_count += 1


print(f"Part twp count: {p2_count}")