"""
https://leetcode.com/problems/valid-parentheses/description/
I actually already did this problem when I was working through my coding book but since I didn't immedately
    remember that, I'm going to work through it again
We implement this with a stack. Whenever we see an open parentheses we push it onto the stack. When we see
    a closed parenthese we pop one off the top of the stack. If it matches with our open parenthese then
    we're all good and we continue going through the string. If it doesn't match then our parentheses are
    malformed.
If we get to the end of the string and we have no parentheses in our stack then our parentheses are
    well formed. If there are still parentheses in our stack then its malformed
"""

def matches(f_char, snd_char):
    result = False
    if f_char == "(" and snd_char == ")":
        result = True
    elif f_char == "[" and snd_char == "]":
        result = True
    elif f_char == "{" and snd_char == "}":
        result = True
    return result

def is_valid(s):
    stack = []
    s_list = list(s)
    for char in s_list:
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        elif char == ')' or char == ']' or char == '}':
            if (not matches(stack.pop(), char)):
                return False
    if len(stack) > 0:
        return False
    else:
        return True
    
assert matches("(", ")")
assert matches("{", "}")
assert matches("[", "]")
assert not matches("[", ")")

assert is_valid("()")
assert is_valid("()[]{}")
assert not is_valid("(]")
assert is_valid("([])")