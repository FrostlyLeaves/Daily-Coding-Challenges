from my_bst import BST
import math
"""

Stick any abandoned elements onto the side arrays. Ex, you've inserted elements with *'s. 
    [1,2,*3,4,*5,6,*7,8]. Stick 1,2,4 together, and 6, 8 together

First get the indicies of the elements we want to push to the BST. The indicies should be ordered such
    that, if you go through the list of indicies and push them in that order, the BST will be height
    balanced.
Find the middle value of the array. If there are an even number of elements then get the middle
    rounded up (5 in [4, 5]).
To get the list of indicies we need to make a list from range(len(array))    
"""
array1 = [1,2,3,4,5,6,7,8]
array2 = [1,2,3,4,5,6,7]
array3 = [1]

"""
def order_indicies(array, q=[]):
    if len(array) == 0:
        return []
    if len(q) != 0:
        q.pop()
    i_mid = math.floor(len(array)/2)
    q.append(array[i_mid])
    return [array[i_mid]] + order_indicies(array[:i_mid]) + order_indicies(array[i_mid + 1:])

print(order_indicies(array1))
"""

def order_indicies(array):

    # Base Case
    if len(array) == 0:
        return []

    # Create an empty queue
    # for level order traversal
    queue = []
    result = []
    temp = []
    left = []
    right = []

    # Enqueue Root and initialize height
    queue.append(array)

    while(len(queue) > 0):

        # Print front of queue and
        # remove it from queue
        temp = queue.pop(0)
        i_mid = math.floor(len(temp)/2)
        result.append(temp[i_mid])

        # Enqueue left child
        left = temp[:i_mid]
        if len(left) != 0:
            queue.append(left)

        # Enqueue right child
        right = temp[i_mid + 1:]
        if len(right) != 0:
            queue.append(right)
    return result

print(order_indicies(array1))    
print(order_indicies(array2))    
print(order_indicies(array3))

def make_hb_bst(ordered_array):
    bst = BST()
    for x in ordered_array:
        bst.insert(x)
    return bst

bst = make_hb_bst(order_indicies(array1))
print(bst.get_root().data)
print(bst.get_root().left.data)
print(bst.get_root().right.data)
print(bst.get_root().left.left.data)
print(bst.get_root().left.right.data)
print(bst.get_root().right.left.data)
print(bst.get_root().right.right.data)
print(bst.get_root().left.left.left.data)

"""
print()
print(array1[5:])
i_mid = math.floor(len(array1[5:])/2)
print(array1[5:][i_mid+1:])
i_mid2 = math.floor(len(array1[5:][i_mid+1:])/2)
print(array1[5:][i_mid+1:][i_mid2+1:])

print(array1[:4])
i_mid3 = math.floor(len(array1[:4])/2)
print(array1[:4][:i_mid3])
i_mid4 = math.floor(len(array1[:4][:i_mid3])/2)
print(array1[:4][:i_mid3][:i_mid4])
i_mid5 = math.floor(len(array1[:4][:i_mid3][:i_mid4])/2)
print(array1[:4][:i_mid3][:i_mid4][:i_mid5])
"""