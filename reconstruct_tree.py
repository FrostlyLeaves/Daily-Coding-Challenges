"""

"""

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree = Node('a', Node('b', Node('d'), Node('e')), Node('c', Node('f'), Node('g')))


def in_order(node):
    if (node.left != None):
        in_order(node.left)
    print(node.data)
    if (node.right != None):
        in_order(node.right)

def pre_order(node):
    print(node.data)
    if (node.left != None):
        pre_order(node.left)
    if (node.right != None):
        pre_order(node.right)

"""
in-order:
-leftmost. That one's parent. That one's sibling. parent's parent.
-make a node, a. Make a node, b, and have a be left child. made a node, c, and have it be b's right child. Make a node, d,

-have a boolean "left". If true then we 

-have a parent and cur node passed in. If both cur_node's children are None then look to the parent. If the parent is None then
    grab the next item in the list. That's the parent. Make cur_node the left child. Call on parent. If have only left child
    then grab next thing in list. Make that right child

    
Pre = pre order. In = in order

First element of Pre is always root. Second element is either left or right child. It's the right child if the first element of
    In is also the root. Otherwise it's the left
    
"""

tree2 = Node('a', Node('b', None, Node('d')), Node('c'))
tree3 = Node('a', None, Node('c', Node('f'), Node('g')))

Pre = "abdecfg"
In = "dbeafcg"

print(Pre[1: 4])
print(In[0:3])