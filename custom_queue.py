import random 

CAPACITY = 10
class CustomQueue:
    def __init__(self, capacity:int=CAPACITY):
        self.capacity = capacity
        self._items = []

    def is_full(self):
        return len(self._items) == self.capacity
    
    def is_empty(self) :
        return not self._items

    def enqueue(self, x):
        if self.is_full():
            raise OverflowError("queue is full")
        self._items.append(x)
    
    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)
        
    def front(self):
        if self.is_empty():
            return None 
        return self._items[0]

    def back(self):
        if self.is_empty():
            return None 
        return self._items[len(self._items)-1]

