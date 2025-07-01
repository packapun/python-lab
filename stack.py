import random 

class Stack:
    def __init__(self, capacity:int=10):
        self.capacity = capacity
        self._items = []

    def __str__(self):
        return "{}".format(self._items)

    def isFull(self):
        return len(self._items) == self.capacity
    
    def isEmpty(self) :
        return len(self._items) == 0

    def push(self, x:int):
        if self.isFull():
            print("[warning] stack is full")
            return 
        self._items.append(x)
    
    def pop(self):
        if self.isEmpty():
            print("[warning] stack is empty")
            return None
        return self._items.pop()
    
    def peek(self):
        if self.isEmpty():
            return None 
        return self._items[len(self._items) - 1]


s = Stack(capacity=10)
data = [random.randint(0,x) for x in range(1,20)]
[s.push(x) for x in data]
print(s)
[s.pop() for x in data]
print(s)








    

