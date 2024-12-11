grid = []

with open('8_input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.strip('\n')))

# build map of {letter: [coords]}
map = {}
for irow, row in enumerate(grid):
    for icol, char in enumerate(row):
        if char != '.':
            if char in map:
                map[char].append((irow, icol))
            else:
                map[char] = [(irow, icol)]


for letter, coords in map.items():
    for idx, coord in enumerate(coords):
        for idx2, coord2 in enumerate(coords):
            if coord2[1] == coord[1] and coord2[0] == coord[0]: continue
            dx = coord2[1] - coord[1]
            dy = coord2[0] - coord[0]

            an = (coord2[0]+dy, coord2[1]+dx)

            if 0 <= an[0] < len(grid) and 0 <= an[1]<len(grid[0]):
                grid[an[0]][an[1]] = '#'

p1_count = 0

for y, i in enumerate(grid):
    for x, j in enumerate(i):
        if j == '#':
            p1_count += 1

print(f"Part one count: {p1_count}")

for letter, coords in map.items():
    for idx, coord in enumerate(coords):
        for idx2, coord2 in enumerate(coords):
            if coord2[1] == coord[1] and coord2[0] == coord[0]: continue
            dx = coord2[1] - coord[1]
            dy = coord2[0] - coord[0]

            grid[coord[0]][coord[1]] = '#'
            grid[coord2[0]][coord2[1]] = '#'

            an = (coord2[0]+dy, coord2[1]+dx)

            while 0 <= an[0] < len(grid) and 0 <= an[1]<len(grid[0]):
                grid[an[0]][an[1]] = '#'
                an = (an[0]+dy, an[1]+dx)

p2_count = 0

for y, i in enumerate(grid):
    for x, j in enumerate(i):
        if j == '#':
            p2_count += 1

print(f"Part two count: {p2_count}")