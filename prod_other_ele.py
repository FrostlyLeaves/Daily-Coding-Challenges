x = [1,2,3,4,5]
y = [3, 2, 1]

"""
Program that takes a position and a list. Returns the product of
    all places in that list minus that position
"""
def prod(position, list):
    result = 1
    for p in range(len(list)):
        if (p != position):
            result *= list[p]
    return result

"""
Function that takes a list and return a list of that same size. Each
    element is the product of all other elements in that list

"""
def prod_list(list):
    result = [-1] * len(list)
    for i in range(len(list)):
        result[i] = prod(i, list)
    return result

print(prod_list(x))
print(prod_list(y))
print(x[-1])