"""
https://leetcode.com/problems/merge-two-sorted-lists/description/
This code was written in a rush. Here are some scrap notes:
    Whenever we add an element from a list to result we increment that list's sential value.
        -for each loop we always add an element to result and we alawys increment a sential value
"""

def merge_sorted_lists(list1, list2):
    result = []
    i = j = 0
    while (i +1 == len(list1) and j + 1 == len(list2)) or (len(result) < len(list1) + len(list2)):
        if i +1 > len(list1):
            result.append(list2[j])
            j +=1
        elif j +1 > len(list2):
            result.append(list1[i])
            i += 1 
        elif (list1[i] <= list2[j]):
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1
    return result

assert merge_sorted_lists([1,2,4], [1,3,4]) == [1,1,2,3,4,4]
assert merge_sorted_lists([], []) == []
assert merge_sorted_lists([], [0]) == [0]