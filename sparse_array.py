"""
Use a hash table. Don't track the 0's. If they try to "get" an element that's over the size of the
    array (or less than 0) then return an out of range error. If they try to access an element in
    the size that hasn't been set then just return 0.
"""

class Sparse:
    def __init__(self, arr, size):
        self.size = size
        self.h = {}
        for i in range(len(arr)):
            if (arr[i] != 0):
                self.h[str(i)] = arr[i]
    
    def set(self, i, val):
        if ((i > size) or (i < 0)):
            raise IndexError("The specified index i is out of the range of the array")
        self.h[str(i)] = val
    
    def get(self, i):
        result = 0
        if ((i > size) or (i < 0)):
            raise IndexError("The specified index i is out of the range of the array")
        elif (str(i) in self.h):
            result = self.h[str(i)]
        return result

x = [0,0,0,0,0,0,0,0,4,0,0,0,5,0,0,0,0,1,0,0,1,0,0,0,0,0,0,7]
size = len(x)

s = Sparse(x, size)
print(s.get(8))
print(s.get(0))
s.set(0, 5)
print(s.get(0))
s.set(8, 2222)
print(s.get(8))
print(s.get(27))