class Max_Stack:
    max_val = -1
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)
        if x > self.max_val:
            self.max_val = x
    
    def pop(self):
        return self.stack[0]
    
    def max(self):
        if (self.max_val == -1):
            raise("The stack is empty. There is no max value.")
        return self.max_val
    
ms = Max_Stack()
#ms.max()
ms.push(3)
ms.push(5)
ms.push(5)
print(ms.pop())
print(ms.max())