"""
Given the head of a singly linked list, reverse it in-place
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

head = Node("head", Node("John", Node("Paul", Node("Ringo"))))

"""
Previous, cur, temp1, temp2. 
temp1 = cur.next.
cur.next = previous

temp2 = cur
cur = temp1
previous = temp2

"""

head2 = Node("Jesus")

def reverse_ll(oldHead):
    curNode = previous = temp1 = temp2 = Node
    curNode = oldHead
    previous = None
    while(curNode != None):
        temp1 = curNode.next
        curNode.next = previous

        temp2 = curNode
        curNode = temp1
        previous = temp2
    return previous

fart = reverse_ll(head)
fart2 = reverse_ll(head2)

print(fart.data)
print(fart.next.data)
print()
print(fart2.data)
print(fart2.next)