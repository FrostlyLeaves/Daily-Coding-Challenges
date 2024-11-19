"""
We have a theoretical list of increasing elements from 0 to N where N = list length - 1. [0,1,2, . . . N]. This
    list has been jumbled up. The only indication we have as to its new order is a list of +'s and -'s. Each +
    or - indicates if that position's element is greater or less than the previous element. So, [None, +, +, -, +]
    could be [1,2,3,0,4]. Note that the elements in the resulting list have to be the same from our o.g. list, 
    [0,1,2, . . . N].

Go through and count the number of -'s. Have our first number be this number. The range of values that each
    + value can be is all numbers above the number of -'s. The range of values that each - value can be is
    all numbers below the number of -'s.
    The first - value is -1 the number of -'s. Each subsequent - value is -1 the previous - value. The first + value
    is 1 + the number of -'s. Each subsequent + value is 1 + the previous + value.

"""

def find_neg_num(list):
    result = 0
    for x in list:
        if (x == "-"):
            result += 1
    return result

def plus_neg_to_array(list):
    result = []
    pre_plus = pre_minus = -1
    neg_num = find_neg_num(list)
    if len(list) == 0:
        return result
    for x in list:
        if x == None:
            result.append(neg_num)
            pre_plus = neg_num
        elif (pre_minus == -1) and (x == "-"):
            result.append(neg_num-1)
            pre_minus = neg_num - 1
        elif (pre_minus != -1) and (x == "-"):
            result.append(pre_minus - 1)
            pre_minus -= 1
        elif (x == "+"):
            result.append(pre_plus+1)
            pre_plus +=1
    return result

list = [None, "+", "+", "-", "+"]
list1 = [None, "+", "+", "+", "+"]
list2 = [None, "-", "-", "-", "-"]

print(plus_neg_to_array(list))
print(plus_neg_to_array(list1))
print(plus_neg_to_array(list2))