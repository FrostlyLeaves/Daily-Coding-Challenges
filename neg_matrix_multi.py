import math
import sys
"""
https://leetcode.com/problems/maximum-matrix-sum/?envType=daily-question&envId=2024-11-24
If there are no negatives, we're golden. Return the sum
If there are an even # of negatives then move and multiply them such that there are none
If there are an odd # of negs move and multiply such that there is 1 neg. Find the
    smallest value. Move the neg to this smallest value
"""

def find_num_neg(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < 0:
                count += 1
    return count

m1 = [[1,-1],
      [-1,1]]
m2 = [[1,2,3],
      [-1,-2,-3],
      [1,2,3]]
m3 = [[1,1],
      [1,1]]
m4 = [[-1,2,3],
      [1,2,3],
      [1,2,-3]]
m5 = [[3,2,3],
      [3,2,3],
      [1,2,-3]]


"""
For an abritrary element in a matrix, m[i][j]. The elements around it are m[i-1][j] (on to above),
    m[i][j-1] (one to the left), m[i+1][j] (one below), m[i][j+1] (one to the right)
"""


def make_positive(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if (matrix[i][j] < 0):
                if ((i-1 >=0) and (matrix[i-1][j] < 0)):
                    matrix[i][j] *= -1
                    matrix[i-1][j] *= -1
                elif ((j-1 >=0) and (matrix[i][j-1] < 0)):
                    matrix[i][j] *= -1
                    matrix[i][j-1] *= -1
                elif ((i+1 < len(matrix)) and (matrix[i+1][j] < 0)):
                    matrix[i][j] *= -1
                    matrix[i+1][j] *= -1
                elif ((j+1 < len(matrix[i])) and (matrix[i][j+1] < 0)):
                    matrix[i][j] *= -1
                    matrix[i][j+1] *= -1
    return matrix

"""
Move
-find a neg number: x
-find closest neg number:
-repeatedly multiply x (and neigbor (new x)) so it's closer to y
-once x and y are adjacent, mulitply both by -1
"""
def find_neg_el(matrix):
    i = j = 0
    while matrix[i][j] >=0:
        if j == (len(matrix[i]) - 1):
            j = 0
            i +=1
        elif i == ((len(matrix)) - 1) and j == (len(matrix[i]) - 1):
            raise ValueError("No negative in matrix")
        else:
            j += 1
    return [i, j]

def find_closest_neg(matrix, point):
    brk = False
    off_set = [0, 0]
    for n in range(1, len(matrix)):
        if brk:
            break
        combinations = [[x, y] for x in range(-n, n + 1) for y in range(-n, n + 1) if abs(x) == n or abs(y) == n]
        for position in combinations:
            if (0 <= (point[0] + position[0])) and \
                (0 <= (point[1] + position[1])) and \
                (len(matrix) > (point[0] + position[0])) and \
                (len(matrix[0]) > (point[1] + position[1])):
                if matrix[point[0] + position[0]][point[1] + position[1]] < 0:
                    off_set = position
                    brk = True
                    break
    return off_set

def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def move(matrix, start, end):
    cur_position = start.copy()
    cur_dis = len(matrix) + 1
    pos_move = [len(matrix) +1, len(matrix) + 1]
    possible_moves = [(0,1),(0,-1),(1,0),(-1,0)]
    while (distance(cur_position, end)) != 1:
        cur_dis = len(matrix) + 1
        for pm in possible_moves:
            if (0 <= (cur_position[0] + pm[0])) and \
                (0 <= (cur_position[1] + pm[1])) and \
                (len(matrix) > (cur_position[0] + pm[0])) and \
                (len(matrix[0]) > (cur_position[1] + pm[1])):
                if distance(end, [cur_position[0] + pm[0], cur_position[1] + pm[1]]) < cur_dis:
                    pos_move[0], pos_move[1] = pm[0], pm[1]
                    cur_dis = distance(end, [cur_position[0] + pm[0], cur_position[1] + pm[1]])
        matrix[cur_position[0] + pos_move[0]][cur_position[1] + pos_move[1]] *= -1
        matrix[cur_position[0]][cur_position[1]] *= -1
        cur_position[0] += pos_move[0]
        cur_position[1] += pos_move[1]
    return cur_position


def find_smallest_el(matrix):
    smallest = sys.maxsize
    smallest_pos = [-1,-1]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if abs(matrix[i][j]) < smallest:
                smallest = abs(matrix[i][j])
                smallest_pos[0], smallest_pos[1] = i, j
    return smallest_pos

def matrix_sum(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
    return sum

def maxMatrixSum(matrix):
    num_neg = find_num_neg(matrix)
    is_odd = True
    r = list(range(math.floor(num_neg/2)))
    if num_neg % 2 == 0:
        is_odd = False
    for _ in r:
        p1 = find_neg_el(matrix)
        p2 = find_closest_neg(matrix, p1)
        p3 = move(matrix, p1, [p1[0] + p2[0], p1[1] + p2[1]])
        matrix[p1[0] + p2[0]][p1[1] + p2[1]] *= -1
        matrix[p3[0]][p3[1]] *= -1
    if is_odd:
        smallest_pos = find_smallest_el(matrix)
        odd_p = find_neg_el(matrix)
        p4 = move(matrix, odd_p, smallest_pos)
        matrix[smallest_pos[0]][smallest_pos[1]] *= -1
        matrix[p4[0]][p4[1]] *= -1
    return matrix_sum(matrix)

print(maxMatrixSum(m1))
print(maxMatrixSum(m2))
print(maxMatrixSum(m4))
print(maxMatrixSum(m5))
print(maxMatrixSum(m3))