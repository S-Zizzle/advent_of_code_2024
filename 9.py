data = []

with open('9_input.txt', 'r') as file:
    for line in file:
        data = list(map(int, line))

#convert
#2333133121414131402
#into
#00...111...2...333.44.5555.6666.777.888899
p1_data = []
id = 0
free = False
for num in data:
    # this is such a bad way to do it. could do loop increment by 2 indexes at a time?
    if not free:
        for i in range(num):
            p1_data.append(id)
        id += 1
        free = True
    else:
        for i in range(num):
            p1_data.append('.')
        free = False

p2_data = p1_data.copy()

#then shuffle numbers left
#0..111....22222
#02.111....2222.
#022111....222..
#0221112...22...
#02211122..2....
#022111222......
'''
p = len(p1_data) - 1

for idx, num in enumerate(p1_data):
    print(idx)
    if num == '.':
        if p1_data[idx:] == ['.'] * (len(p1_data) - idx):
            p1_data = p1_data[:idx]
            break
        
        for i in range(p, 0, -1):
            if p1_data[i] != '.':
                p1_data[idx] = p1_data[i]
                p1_data[i] = '.'
                p = i
                break

p1_checksum = sum(i * v for i, v in enumerate(p1_data))
print(f"Part one total: {p1_checksum}")
      '''

# part two only move whole files, start with highest id
#00...111...2...333.44.5555.6666.777.888899
#0099.111...2...333.44.5555.6666.777.8888..
#0099.1117772...333.44.5555.6666.....8888..
#0099.111777244.333....5555.6666.....8888..
#00992111777.44.333....5555.6666.....8888..

# this will melt you cpu if you run this
# need to create a map of where the free spaces are, then in the loop when we know the length of the numbers to move
# we just check if there is space in the map, if there is swap the values
for i in range(len(p2_data)-1, 0, -1):
    #print(i)
    if p2_data[i] != '.':
        for j in range(i, 0, -1):
            if p2_data[j] != p2_data[i-1]:
                size = i-j
                count = 0
                for m in range(0, j, 1):
                    print(i, j, m)
                    if p2_data[m] == '.':
                        count += 1
                        if count == size:
                            p2_data[m-count-1:m] = p2_data[j:i+1]
                            p2_data[j:i+1] = ['.'] * count
                    else:
                        count = 0

p2_checksum = sum(i * v for i, v in enumerate(p2_data))
print(f"Part two total: {p2_checksum}")