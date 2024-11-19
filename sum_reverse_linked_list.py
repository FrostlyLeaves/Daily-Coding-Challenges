class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

"""
Use recursion
"""

twenty_five = Node(5, Node(2))
ninety_nine = Node(9, Node(9))

def one_ll_sum_internal(nde, pos):
    if (nde.next == None):
        return nde.data * 10**pos
    else:
        return nde.data * 10 ** pos + one_ll_sum_internal(nde.next, pos+1)

def one_ll_sum(nde):
    return one_ll_sum_internal(nde, 0)

"""
do a while loop
"""

def make_ll(val):
    nde = resultish = Node(0)
    while(val != 0):
        nde.next = Node(val % 10)
        val = val - val % 10
        val = val // 10
        nde = nde.next
    return resultish.next

def make_ll_sum(head1, head2):
    sum = one_ll_sum(head1) + one_ll_sum(head2)
    return make_ll(sum)

bob = make_ll_sum(twenty_five, ninety_nine)
print(bob.data)
print(bob.next.data)
print(bob.next.next.data)



