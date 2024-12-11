data = []

with open('9_input.txt', 'r') as file:
    for line in file:
        data = list(map(int, line))

#convert
#2333133121414131402
#into
#00...111...2...333.44.5555.6666.777.888899
longlist = []
id = 0
free = False
for num in data:
    # this is such a bad way to do it. could do loop increment by 2 indexes at a time?
    if not free:
        for i in range(num):
            longlist.append(id)
        id += 1
        free = True
    else:
        for i in range(num):
            longlist.append('.')
        free = False

#then shuffle numbers left
#0..111....22222
#02.111....2222.
#022111....222..
#0221112...22...
#02211122..2....
#022111222......

for i in longlist:
    if i == '.':
        # check if every value after this is a '.'. if so we are finished. break out the loop and chop the end of the list of so its only numbers
        pass #find the index of last number
        # replace this index with the last number and set last number index to a '.'


#then calculate checksum
# sum(index * value)