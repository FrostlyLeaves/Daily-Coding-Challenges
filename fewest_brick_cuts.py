"""
Have a list that keeps track of the number of bricks that end at each brick position, num_pos
The height of the wall is just the length of the first list (in the brick wall matrix)
The maxium of num_pos will be the maximum bricks all ending in that same position. The height
    minus this will be our fewest number of cuts
"""

def find_min_cuts(wall):
    height = len(wall)
    length = sum(wall[0])
    num_pos = [0]*length
    position = 0
    for i in range(height):
        for j in range(len(wall[i])):
            position += wall[i][j]
            #all of them are going to end at the end of the brick wall so we're ignoring that bit
            if (position != length):
                num_pos[position] += 1
        position = 0
    return height - max(num_pos)

wall = [[3,5,1,1],
        [2,3,3,2],
        [5,5],
        [4,4,2],
        [1,3,3,3],
        [1,1,6,1,1]]

print(find_min_cuts(wall))