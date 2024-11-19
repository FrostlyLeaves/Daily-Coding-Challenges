from my_bst import *

"""
Let's call the value that we're trying to find the floor and ceiling of, v.
For floor and ceiling, compare the current node. (if v = cur_node then just return that) If v < cur_node go to the 
    left child. If v > cur_node than go to the right node. If we can't then we stop.
    Have a floorist value. Initally set it to None. For each node, if 
    floorist < cur_node < v, then floorist = cur_node value
    -if floorist == None and cur_node < v then floorist = cur_node value
    When we stop, return floorist
    Have a ceilingist value. Initally set it to None. For each node, if
    v < cur_node < celingist, then ceilingist = cur_node value.
    -if ceilingist == None and cur_node > v then ceilingist = cur_node value 
"""

def floor_and_ceiling(node, val, ceilingist=None, floorist=None):
    if not node:
        return None, None
    elif (val == node.data):
        return node.data, node.data
    elif ((ceilingist == None) and (node.data > val)):
        ceilingist = node.data
    elif ((floorist == None) and (node.data < val)):
        floorist = node.data
    elif ((val < node.data) and (node.data < ceilingist)):
        ceilingist = node.data
    elif ((floorist < node.data) and (node.data < val)):
        floorist = node.data
    
    if node.left and (val < node.data):
        return floor_and_ceiling(node.left, val, ceilingist, floorist)
    elif node.right and (val > node.data):
        return floor_and_ceiling(node.right, val, ceilingist, floorist)
    else:
        return floorist, ceilingist

tree1 = BST()
tree1.insert(7)
tree1.insert(5)
tree1.insert(10)
tree1.insert(-1)
tree1.insert(6)
tree1.insert(25)
f, c = floor_and_ceiling(tree1.get_root(), 5.5)
print(str(f) + " " + str(c))

tree2 = BST()
tree2.insert(7)
tree2.insert(-1)
tree2.insert(10)
tree2.insert(-5)
tree2.insert(4)
tree2.insert(9)
tree2.insert(15)
tree2.insert(7.1)
tree2.insert(3.8)
tree2.insert(4.5)
tree2.insert(4.3)
tree2.insert(4.6)
tree2.insert(6)
f, c = floor_and_ceiling(tree2.get_root(), 5)
print(str(f) + " " + str(c))
f, c = floor_and_ceiling(tree2.get_root(), 8)
print(str(f) + " " + str(c))


tree3 = BST()
tree3.insert(10)
tree3.insert(-5)
tree3.insert(-4)
tree3.insert(4)
tree3.insert(9)
tree3.insert(9.5)
tree3.insert(8)
tree3.insert(7)
f, c = floor_and_ceiling(tree3.get_root(), 5)
print(str(f) + " " + str(c))

tree4 = BST()
tree4.insert(10)
tree4.insert(9)
tree4.insert(8)
tree4.insert(7)
tree4.insert(-5)
tree4.insert(-3)
f, c = floor_and_ceiling(tree4.get_root(), 5)
print(str(f) + " " + str(c))

tree5 = BST()
tree5.insert(10)
f, c = floor_and_ceiling(tree5.get_root(), 5)
print(str(f) + " " + str(c))

tree6 = BST()
f, c = floor_and_ceiling(tree6.get_root(), 5)
print(str(f) + " " + str(c))