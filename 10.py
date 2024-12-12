grid = []

with open('10_input.txt', 'r') as file:
    for line in file:
        grid.append(list(map(int, line.strip('\n'))))

#find the 0's
zeros = []
for irow, row in enumerate(grid):
    for icol, char in enumerate(row):
        if char == 0:
            zeros.append((irow, icol))

def recurse(coord):
    r = coord[0]
    c = coord[1]
    v = grid[r][c]
    p = []

    # is this the neatest way to check within bounds? i don't think so
    if 0 <= r-1 < len(grid) and 0 <= c < len(grid[0]):
        if grid[r-1][c] == v + 1: #top
            p.append(recurse((r-1, c)))
    if 0 <= r < len(grid) and 0 <= c+1 < len(grid[0]):
        if grid[r][c+1] == v + 1: #right
            p.append(recurse((r, c+1)))
    if 0 <= r+1 < len(grid) and 0 <= c < len(grid[0]):
        if grid[r+1][c] == v + 1: #bottom
            p.append(recurse((r+1, c)))
    if 0 <= r < len(grid) and 0 <= c-1 < len(grid[0]):
        if grid[r][c-1] == v + 1: #left
            p.append(recurse((r, c-1)))
    
    return p

routes = {}

for zero in zeros:
    nines = recurse(zero)

    for nine in nines:
        if zero in routes: routes[zero].append(nine)
        else: routes[zero] = [nine]

total = 0

for x, y in routes.items():
    total += len(y)

print(total)