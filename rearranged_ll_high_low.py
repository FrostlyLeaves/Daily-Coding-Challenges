class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

"""
Have a boolean that's "looking_for_low"
Find the next node that's higher/lower
Remove the node. Node before points to next node
Insert the node. Node we're looking at points to target node. Target node points to one after current
If there is no higher/lower node then just leave the node where it is
"""


test = Node(1, Node(2, Node(3, Node(4, Node(5)))))

def find_target_node(nde, looking_for_high):
    target = None
    value = nde.data
    if (looking_for_high):
        while((nde.next != None) & (value >= nde.data) ):
            nde = nde.next
            if (value < nde.data):
                target = nde
    else:
        while((nde.next != None) & (value <= nde.data)):
            nde = nde.next
            if (value > nde.data):
                target = nde
    return target

print(find_target_node(test.next, False))

"""
def make_low_high(nde):
    looking_for_high = True
    pre_nde = None
    target_node = pre_target = after_nde = Node
    while(nde.next != None):
        target_node = 
        """