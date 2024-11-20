import math

"""
I'm not going to use a heap. I'm going to use quickselect. I'm going to change it a little bit so it's
    online (doesn't need the whole list to run and runs as it's steadily fed the rest of the list)
Quickselect steps:
-find the index of the list you want. If it's odd length then just the middle element (ex. length 3,
    want index 1 [0,1,2]). If it's even then want the two middle elements (ex. length 4, want index
    1 and 2 [0,1,2,3])
-pick a pivolt, p
-put all elements less than p on to the left of it and all elements greater than p to its right. If
    p's index value is less than/greater than the index you want then recurse on the left/right side
    of the list.
    -continue this until you've found your elements and index/ices
-CHANGES TO MAKE IT ONLINE
    -keep track of your middle element(s) and their index/ices
    -with each new element you'll either have to find the element & index one to the left of our
        saved element(s) & index/ices or one to the right. Do this and update our saved element(s)
        & index/ices
"""


def partition(list, l_i, r_i):
    pivot = list[l_i]
    p_i = l_i
    for j in range(l_i, r_i):
        if (list[j] < list[p_i]):
            if (abs(p_i - j) > 1): #If the next el to swap with is more than 1 el away
                list[p_i], list[p_i + 1], list[j] = list[j], list[p_i], list[p_i+1]
                p_i += 1
            else:
                list[p_i], list[j] = list[j], list[p_i]
                p_i += 1
    return [list, p_i]

#Return the changed list, middle element, and middle index
def quickselect(list):
    median = 0
    
    index = math.floor((len(list)-1)/2)
    p_i = -1
    left = 0
    right = len(list)
    while index != p_i:
        list, p_i = partition(list, left, right)
        if index < p_i:
            right = p_i #would be p_i -1 but because of off by 1 it isn't
        elif index > p_i:
            left = p_i + 1
    
    median = list[p_i]

    print(list)

    #If it's even then find the other
    #This part is really dumb! I think that if I just searched the space between p_i and the "right" value
    #   then I'd pretty quickly find the next median value! I worked on this for a while and couldn't
    #   flipin' do it so I just copied this code
    #Note to myself: all those numbers between [p_i, right] contain the next highest element from p_i
    if (len(list) % 2 == 0):
        index2 = math.ceil((len(list)-1)/2)
        while index2 != p_i:
            list, p_i = partition(list, left, right)
            if index2 < p_i:
                right = p_i #would be p_i -1 but because of off by 1 it isn't
            elif index2 > p_i:
                left = p_i + 1
        median = (median + list[p_i])/2
    
    print(median)
    print()

l = [2,1,5,7,2,0,5]
quickselect(l)

l2 = [1,2,3,4]
quickselect(l2)

l3 = [212, 8, 161, 752, 722, 854, 468, 455, 881, 878]
quickselect(l3)