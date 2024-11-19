import math

"""
Made a new class, hv, that takes a height and a value
Traverse the tree. For each node, add an hv to a list
Go through the list and sum each value at each height
-just do a for loop of the list and have another list that tracks each height's sum
Go through the list of sums and return the index of the value that has the minimum sum
"""

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class HV:
    def __init__(self, value, height):
        self.value = value
        self.height = height

def make_hv_list(node, height=0):
    if node == None:
        return []
    else:
        return [HV(node.data, height)] + make_hv_list(node.left, height+1) + make_hv_list(node.right, height + 1)

def find_height(list):
    height = 0
    for x in list:
        if x.height > height:
            height = x.height
    return height

def find_sums(list):
    sum_list = [0]*(find_height(list)+1)
    for x in list:
        sum_list[x.height] += x.value
    return sum_list

def find_min_index(sum_list):
    index = 0
    for i in range(len(sum_list)):
        if (sum_list[i] < sum_list[index]):
            index = i
    return index

tree1 = Node(1, Node(2), Node(3, Node(4), Node(5)))
tree2 = Node(35, Node(0, Node(7)))
tree3 = Node(10, Node(3, Node(0), Node(0)), Node(3, Node(0), Node(0)))

print(find_min_index(find_sums(make_hv_list(tree1))))
print(find_min_index(find_sums(make_hv_list(tree2))))
print(find_min_index(find_sums(make_hv_list(tree3))))