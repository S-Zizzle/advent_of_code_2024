grid = []

with open('12_input.txt', 'r') as file:
    for line in file:
        grid.append(list(line.strip('\n')))

map = {}

for irow, row in enumerate(grid):
    for icol, val in enumerate(row):
        if val not in map:
            map[val] = [0, 0]
        
        map[val][0] += 1
        
        if irow != 0 and irow != len(grid)-1:
            if grid[irow-1][icol] != val:
                map[val][1] += 1
            if grid[irow+1][icol] != val:
                map[val][1] += 1
        else:
            map[val][1] += 1
        
        if icol != 0 and icol != len(grid[0])-1:
            if grid[irow][icol+1] != val:
                map[val][1] += 1
            if grid[irow][icol-1] != val:
                map[val][1] += 1
        else:
            map[val][1] += 1
        
total = 0

for key, values in map.items():
    total += values[0] * values[1]

print(total)