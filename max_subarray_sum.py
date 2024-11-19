from functools import reduce
from operator import add

x = [34,-50,42,14,-5,86]

def max_subarray_sum(array):
    max = 0
    for i in range(len(x)):
        for j in range(i, len(x)):
            sub_sum = reduce(add, x[i:j+1])
            if (max < sub_sum):
                max = sub_sum
    return max

print(max_subarray_sum(x))
