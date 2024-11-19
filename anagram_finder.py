"""
Put each character into a dictionary. Have each value be the number of times that character shows up. Have the first element be 
   the number of characters in the word
Go through the string. Make a copy of the dictionary.
-for each character, 
    -if that character is in the word, subtract 1 from that element in the copied dictionary and from the copied dictionary's
        length
    -if that character isn't in the word, remake the copied dictionary from the dictionary
    -if the copied dictionary's length is 0, remake the copied dictionary and add a starting place of the current element in
        the list minus the word length
"""


def find_anagrams_start(s, word):
    result = []
    temp = dict = {}   
    dict['len'] = len(word)
    for x in word:
        if x in dict:
            dict[x] +=1
        else:
            dict[x] = 1
    temp = dict.copy()
    for i in range(len(s)):
        if (s[i] in temp):
            temp[s[i]] -=1
            temp['len'] -=1
        else:
            temp = dict.copy()
        if (temp['len'] == 0):
            result.append(i - len(word) + 1)
            temp = dict.copy()
    return result

s = "abxaba"
word = "ab"

print(find_anagrams_start(s, word))