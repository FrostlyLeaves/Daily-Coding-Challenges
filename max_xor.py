from sys import maxsize


def max_xor(integers):
    max = -maxsize
    values = [0 , 0]
    for x in integers:
        for y in integers:
            if x ^ y > max:
                max = x ^ y
    return max

print(max_xor([1,2,3,4,5,6,7]))