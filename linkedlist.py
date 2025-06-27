# Let's implement a Linked List 
import random

# Define the node data structure
class Node:
    def __init__(self, data, ptr):
        self.ptr = ptr 
        self.data = data

# Define the linked list data structure
class LinkedList:
    def __init__(self):
        self.root = None

    def __str__(self):
        if self.isEmpty():
            return "Empty Linked List"
        else:
            string = ""
            p = self.root
            while p:
                string += "{}->".format(p.data)
                p = p.ptr
            string += "NULL"
            return string

    def isEmpty(self):
        return self.root is None

    def addNode(self, data):
        newNode = Node(data,None)
        if self.isEmpty():
            self.root = newNode
        else:
            p = self.root 
            while p.ptr:
                p = p.ptr 
            p.ptr = newNode 
        return self.root


def testLinkedList():
    ll = LinkedList()
    # data = [random.randint(1,1000) for x in range(10)]
    data = [x*x for x in range(1,10)]

    for i in data:
        ll.addNode(i)

    print(ll)


testLinkedList()