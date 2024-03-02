import os
import random

def findShortestPath(array, startX, startY):
    # 2d list, each element will be a list with 2 elements. The element at index 0 is the position to check
    # and the element at index 1 is the history of steps to get there

    visited = []
    queue = [[(startY, startX), []]]

    while(len(queue) > 0):
        data = queue.pop()
        y = data[0][0]
        x = data[0][1]

        if([y, x] in visited or maze[y][x] == 'x'): continue

        visited.append([y, x])
        
        if(array[y][x] == 'o'): return data[1]

        currPath = data[1] + [[y, x]]
        
        # up
        if(y > 0): queue.insert(0, [(y-1, x), currPath])
        # down
        if(y < len(array) -1): queue.insert(0, [(y+1, x), currPath])
        # left
        if(x > 0): queue.insert(0, [(y, x-1), currPath])
        # right
        if(x < len(array[0])-1): queue.insert(0, [(y, x+1), currPath])

# shows the path in a sequence
def visualizeShortestPath(array, path):
    output = array[:]
    
    for i in range(len(path)): 
        os.system('clear')
        # output[path[i][0]][path[i][1]] = str(i + 1)
        output[path[i][0]][path[i][1]] = '#'
        for list in output: print(list)
        input()

# Returns a list of coordinates for all empty spaces
def getEmptySpaces(maze):
    availablePos = []

    # adding all empty spots to availablePos
    for y in range(len(maze)):
        for x in range(len(maze[0])):
            if(maze[y][x] == ' '):
                availablePos.append([y, x])

    return availablePos


# Places object in a random part of the maze that isn't occupied
def placeRandomly(maze, objects):
    availablePos = getEmptySpaces(maze)

    # adding all objects to a random available position
    # if there are not enough positions, return false.
    # otherwise, return true
            
    if(len(objects) > len(availablePos)): return False

    for obj in objects:
        # selecting random position
        [y, x] = random.choice(availablePos)
        # placing object in that position
        maze[y][x] = obj
    
    return True
    

def generateMaze(w, h, obstacles):
    maze = []

    # Creating spaces in maze
    for i in range(h):
        maze.append([])
        for j in range(w):
            maze[i].append(' ')

    # List with all the obstacles and the end of the maze
    obstaclesAndEndList = ['o']
    for i in range(obstacles): obstaclesAndEndList.append('x')

    # Generating obstacles randomly
    placeRandomly(maze, obstaclesAndEndList)

    return maze

while True:
    try:
        print('Enter maze width (press enter to exit): ', end='')
        w = input()
        if(w == ''): break
        w = int(w)
        print('Enter maze height: ', end='')
        h = int(input())
        print('Enter amount of obstacles: ', end='')
        obs = int(input())

        maze = generateMaze(w, h, obs)

        # getting shortest path
        [y, x] = random.choice(getEmptySpaces(maze)) # Getting random starting point
        path = findShortestPath(maze, x, y)

        # Displaying results in console
        if(path == None):
            maze[y][x] = "#"
            for list in maze: print(list)
            print("No path was available.")
        else:
            visualizeShortestPath(maze, path)
    except:
        print("Invalid input.")