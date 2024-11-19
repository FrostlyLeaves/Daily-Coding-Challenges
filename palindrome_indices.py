"""
Given a list of words, find all pairs of unique indices such that the concatation of the two words is 
    a palindrome

For example, given the list ["code", "da", "d"], return [(0,1), (1,2), (2,3)].


Make an is_palindrome function

Make a find_palindrome_indicies function
-checks each element against each other element that hasn't been checked yet

"""
list = ["code", "edoc", "da", "d"]


def is_palindrome(str):
    str_len = len(str)
    result = True
    for i in range(str_len//2):
        if (str[i] != str[str_len - 1 - i]):
            result = False
    return result

def find_palindrome_indicies(list):
    result = []
    for i in range(len(list)):
        for j in range(len(list)):
            if (i != j and is_palindrome(list[i] + list[j])):
                print(list[i] + list[j] + " i is %s j is %s" %(i, j))
                result.append((i,j))
    return result

print(find_palindrome_indicies(list))