"""
I'm assuming the tree is full but not necessarily balanced.
    *
  /   \
3      -
      / \
     2   4
Makes sense, 3*(2-4), but
  *
 /
3 
doesn't.


"""

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

tree1 = Node('*', Node('3'), Node('-', Node('2'), Node('4')))
tree2 = Node('*', Node('+', Node('3'), Node('2')), Node('+', Node('4'), Node('5')))

def in_order(node):
    if (node.left != None):
        print("(", end="")
        in_order(node.left)
    print(node.data, end="")
    if (node.right != None):
        in_order(node.right)
        print(")", end="")

def make_equation(node, result=""):
    if (node.left != None):
        result = result + "("
        result = make_equation(node.left, result)
    result = result + node.data
    if (node.right != None):
        result = make_equation(node.right, result)
        result = result + ")"
    return result

bob = make_equation(tree2)
print(bob)
a = eval(bob)

print(a)