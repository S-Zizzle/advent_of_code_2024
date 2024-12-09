import numpy as np

def fileReader(file_path, convert_to_numbers = False):
    with open('6_input.txt', 'r') as file:
        lines = [line.strip() for line in file]
            
        if convert_to_numbers:
            lines = [
                [int(num) for num in line.split()] 
                if line else [] 
                for line in lines
                ]          
        return lines

path = r"C:\Users\dbowg\Desktop\Advent of Code\6\Input.txt"

def mazeToMatrix(maze):
    matrix = np.empty(len(maze),dtype=str)
    for line in maze:
        matrix = np.vstack([matrix,[i for i in line]])
    matrix = np.delete(matrix, (0), axis=0)
    return matrix

def locateGuard(maze):
    return np.argwhere(maze == "^")[0]

def rotateGuard(direction):
    direction = direction.tolist()
    directions = [[-1,0], [0,1], [1,0], [0,-1]]
    curr = directions.index(direction)
    if curr == 3:
        direction = np.array([-1,0])
    else:
        curr+=1
        direction = np.array(directions[curr])

    return direction


def counter(maze):
    direction = np.array([-1,0])
    visited = []
    while True:
        location = locateGuard(maze)
        #print("guard location: ", location)
        visited.append(location.tolist())
        try:
            if maze[(location + direction)[0]][(location + direction)[1]] == ".":
                maze[(location)[0]][(location)[1]], \
                    maze[(location + direction)[0]][(location + direction)[1]] = \
                    maze[(location + direction)[0]][(location + direction)[1]],\
                    maze[(location)[0]][(location)[1]]

            elif maze[(location + direction)[0]][(location + direction)[1]] == "#":
                direction = rotateGuard(direction)
        except IndexError:
            uniqueList = []
            for item in visited:
                if item not in uniqueList:
                    uniqueList.append(item)
            return uniqueList


def main():
    maze = fileReader(path)
    maze = mazeToMatrix(maze)
    visited = counter(maze)
    print(len(visited))
main()


# rather than re-find the guard everytime, once you find it at the start you can just keep pointers for i and j for where he is