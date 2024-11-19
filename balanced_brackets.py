"""
Do it with a stack. If see an open bracket than push it onto the stack. If you see a closed bracket then
    pop the top of the stack off, check with the closed, and continue
"""


def are_brackets_balanced(str):
    brackets = []
    result = True
    str_list = list(str)
    open = ''
    for char in str_list:
        if char in ['(', '[', '{']:
            brackets.append(char)
        elif char in [')', ']', '}']:
            if char == ')':
                open = '('
            elif char == ']':
                open = "["
            elif char == '}':
                open = "{"
            result = result & (brackets.pop() == open)
    if (len(brackets) != 0):
        result = False
    return result

str1 = "([])[]({})"
str2 = "([)]"
str3 = "((()"

print(are_brackets_balanced(str1))
print(are_brackets_balanced(str2))
print(are_brackets_balanced(str3))