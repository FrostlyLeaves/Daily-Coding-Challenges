from my_bst import BST

"""
This is a permutation problem! We just need to find all permutations of the list and insert
    them into the tree. Weirdly, some of these permutations lead to the same tree. For
    example, [2,1,3] and [2,3,1] lead to the same tree. However! I don't want to work on
    this for a long time so I'm just going to use permutations
"""

"""
Function grabbed from this site:
    https://www.geeksforgeeks.org/generate-all-the-permutation-of-a-list-in-python/
"""
# Python function to print permutations of a given list
def permutation(lst):
 
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l

def make_all_BST(n):
    result = []
    values = list(range(1, n + 1))
    p = permutation(values)
    for _ in range(n):
        result.append(BST())

    i = 0
    for l in p:
        for x in l:
            result[i].insert(x)
        i += 1
    return result


bsts = make_all_BST(2)


print(bsts[0].get_root().data)
print(bsts[0].get_root().right.data)
print(bsts[1].get_root().data)
print(bsts[1].get_root().left.data)