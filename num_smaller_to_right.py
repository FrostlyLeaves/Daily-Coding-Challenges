x = [3,4,9,6,1]

def num_smaller_to_right(array):
    result = [0]*len(array)
    for i in range(len(array)):
        count = 0
        for x in array[i+1:]:
            if (array[i] > x):
                count+=1
        result[i] = count
    return result

print(num_smaller_to_right(x))