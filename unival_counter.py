class Node:
    def __init__(self, data, tag, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.tag = tag

"""
Scenarios:
-leaf = +1
-internal node
    -two kids equal each other?
        -no - do nothing
        -yes - check their kids
"""


def same(node):
    if (node.left == node.right == None):
        return True
    if (node.left != None):
        if (node.data == node.left.data):
            return True and same(node.left)
        else:
            return False and same(node.left)
    if (node.right != None):
        if (node.data == node.right.data):
            return True and same(node.right)
        else:
            return False and same(node.right)

tree = Node(0, "John", Node(1, "Mic"), Node(0, "Lucy", Node(1, "Amed", Node(1, "Xi"), Node(1, "Mow")), Node(0, "Tansania")))


print(same(tree))
print(same(tree.left))
print(same(tree.right))
print(same(tree.right.right))
print(same(tree.right.left))

def counter(node, val=0):
    if (node.left == node.right == None):
        return val + 1
    if (node.left != None):
        if (same(node.left)):
            val + 1
        counter(node.left, val)
    if (node.right != None):
        if (same(node.right)):
            val += 1
        counter(node.right, val)
    return val
val = 0
val = counter(tree, val)
print(val)