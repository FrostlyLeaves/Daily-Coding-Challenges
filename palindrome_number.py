import math
"""
https://leetcode.com/problems/palindrome-number/description/
If the number is negative then the result will always be false (you'll never have -1-. That's not a thing)
Get the number of digits of the number, n. Check if the n'th digit is equal to the 1st, the (m-1)'th
    digit is equal to the 2nd, and so on.
"""

def is_neg(num):
    if num < 0:
        return True
    else:
        return False

def is_palindrome(num):
    num_digits = -1
    result = True
    if is_neg(num):
        return False
    
    if num == 0:
        return True
    else:
        num_digits = math.floor(math.log10(abs(num))) + 1
    
    top_num = bottom_num = num
    for _ in range(math.floor(num_digits/2)):
        bottom_digit = bottom_num % 10
        bottom_num = bottom_num // 10

        aug = 10 ** math.floor(math.log10(abs(top_num)))
        top_digit = top_num // aug
        top_num = top_num - top_digit * aug
        if (top_digit != bottom_digit):
            return False
    return True