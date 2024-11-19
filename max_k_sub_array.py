"""
We need to modify Kadane's algoirthm so it roles over and starts a new sub array when we've got a sub array of length
    k. We also need to modify it so that instead of tracking the max value it tracks the array length (and the max 
    value)
Break into multiple steps. If statement. If x > (max_ending_here + x) or (len(max_ending_here_ar) == k), start
    new array and update max_ending_here. Else, add new el to max_ending_here and max_ending_here_ar
"""

def max_sub_array(list, k):
    max_ending_here = max_so_far = 0
    max_ending_here_ar = max_so_far_ar = []
    for x in list:
        if x > (max_ending_here + x) or (len(max_ending_here_ar) == k):
            max_ending_here = x
            max_ending_here_ar.clear()
        else:
            max_ending_here = max_ending_here + x
        max_ending_here_ar.append(x)
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            max_so_far_ar = max_ending_here_ar.copy()
    return max_so_far_ar

arg = [10,5,2,7,8,7]

print(max_sub_array(arg, 3))