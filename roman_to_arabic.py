"""
https://leetcode.com/problems/roman-to-integer/description/
Hard code in the 6 subtraction instances
Make the string into a list and loop over it. For each I add 1, for each V add 5, for each X
    add 10, for each L add 50, for each C add 100, for each D add 500, and for each M add
    1000
"""

def roman_to_arabic(s):
    result = 0
    previous_sub = False
    less_than_length = False
    s_list = list(s)
    for i in range(len(s_list)):
        less_than_length = (i + 1) < len(s_list)
        if previous_sub:
            previous_sub = False
            continue
        elif (less_than_length and (s_list[i] + s_list[i+1])  == "IV"):
            previous_sub = True
            result += 4
        elif (less_than_length and (s_list[i] + s_list[i+1])  == "IX"):
            previous_sub = True
            result += 9
        elif (less_than_length and (s_list[i] + s_list[i+1])  == "XL"):
            previous_sub = True
            result += 40
        elif (less_than_length and (s_list[i] + s_list[i+1])  == "XC"):
            previous_sub = True
            result += 90
        elif (less_than_length and (s_list[i] + s_list[i+1])  == "CD"):
            previous_sub = True
            result += 400
        elif (less_than_length and (s_list[i] + s_list[i+1])  == "CM"):
            previous_sub = True
            result += 900
        elif s_list[i] == "I":
            result +=1
        elif s_list[i] == "V":
            result += 5
        elif s_list[i] == "X":
            result += 10
        elif s_list[i] == "L":
            result += 50
        elif s_list[i] == "C":
            result += 100
        elif s_list[i] == "D":
            result += 500
        elif s_list[i] == "M":
            result += 1000
        else:
            raise ValueError(f"{s_list[i]} is invalid input")
    return result


assert roman_to_arabic("IV") == 4
assert roman_to_arabic("IX") == 9
assert roman_to_arabic("XL") == 40
assert roman_to_arabic("XC") == 90
assert roman_to_arabic("CD") == 400
assert roman_to_arabic("CM") == 900

assert roman_to_arabic("III") == 3
assert roman_to_arabic("LVIII") == 58
assert roman_to_arabic("MCMXCIV") == 1994