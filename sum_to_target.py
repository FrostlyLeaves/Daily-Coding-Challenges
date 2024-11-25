"""
https://leetcode.com/problems/two-sum/description/
Find all two number pairs that sum to "target"
-make a dictionary
    -key = num
    -value = index
Run through our list of numbers
If an element's compliment (target - element) is in our dictionary then we've
    found our pair
Add each element to our dictionary
"""

n1 = [2,7,11,15]
t1 = 9

n2 = [3,2,4]
t2 = 6

n3 = [3,3]
t3 = 6

def two_sum(nums, target):
    seen = {}
    result = [-1, -1]

    for i in range(len(nums)):
        compliment = target - nums[i]
        if compliment in seen:
            result[0], result[1] = i, seen[compliment]
            break
        seen[nums[i]] = i

    return result

print(two_sum(n1, t1))
print(two_sum(n2, t2))
print(two_sum(n3, t3))