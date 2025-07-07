from typing import Optional 

class Node:
    def __init__(self, data:int, next=None):
        self.data = data
        self.next = next 

class LinkedList:
    def __init__(self,head=None):
        self.head = head 
    
    def append(self, x:int):
        if not self.head:
            self.head = Node(x)
            return

        ptr = self.head 
        while ptr.next:
            ptr = ptr.next 

        # ptr now points to the tail of the current linked list
        ptr.next = Node(x)

    def log(self) -> str:
        if not self.head:
            return 
        output = ""
        ptr = self.head 
        while ptr:
            output += "".join(f"{ptr.data}-> ")
            ptr = ptr.next
        output += "NULL"
        return output 


ll = LinkedList()
ll.log()

for i in range(0,12):
    ll.append(i)
print(ll.log())

