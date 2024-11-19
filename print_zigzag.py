"""
make a len(s) x k graph. Fill it all with spaces.
Iterate over the string
Have a "going down" and a "going up" bit
-start at i = j = 0
-for "going down" incriment i and j
    -if j = k -1 then go to "going up"
-for "going_up" increment i and decrement j
    -if j = 0 then go to "going down"

"""

s = "thisisazigzag"

def print_zigzag(s, k):
    result = []
    s_list = list(s)
    going_down = True
    x = y = 0
    for i in range(k):
        temp = [" "]*len(s)
        result.append(temp)

    for i in range(len(s)):
        result[y][x] = s_list[i]
        if (y == k - 1):
            going_down = False
        elif (y == 0):
            going_down = True

        if (going_down):
            x += 1
            y += 1
        else:
            x += 1
            y -= 1

    for row in result:
        for element in row:
            print(element, end=' ')
        print()
        
print_zigzag(s, 5)
