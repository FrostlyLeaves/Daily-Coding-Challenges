"""
https://leetcode.com/problems/longest-common-prefix/description/

Put the first string of the string list into a new list.
For each string after the first, have a while loop and a position, i. While the i-th character of the
    first string and the i-th character of the string we're operating on, match, add that character
    to our final list of characters.
    Return this final list of characters
"""

def longest_prefix(strs):
    result = strs[0]
    for str in strs[1:]:
        i = 0
        temp = ""
        while (i+1 < len(str) and i+1 < len(result)) and result[i] == str[i]:
            temp += result[i]
            i +=1
        result = temp
    
    return result

assert longest_prefix(["flower","flow","flight"]) == "fl"
assert longest_prefix(["dog","racecar","car"]) == ""
assert longest_prefix(["dog"]) == "dog"