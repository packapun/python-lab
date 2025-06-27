import random

class Node:
    def __init__(self, data,left=None, right=None):
        self.left = left 
        self.right = right 
        self.data = data

    def __str__(self):
        return "[{}]".format(self.data)
    
class BinarySearchTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        self.root = self.insertUtil(self.root, data)
    
    def insertUtil(self, root, data):
        if root is None:
            return Node(data)
        if data < root.data:
            root.left = self.insertUtil(root.left,data)
        elif data > root.data: 
            root.right = self.insertUtil(root.right,data)        
        return root 
    
    def inorderTraversal(self,root):
        if root is None:
            return 
        self.inorderTraversal(root.left)
        print(root)
        self.inorderTraversal(root.right)

def testBinarySearchTree():
    tree = BinarySearchTree(Node(10))
    data = [random.randint(1,100) for _ in range(1,10)]
    for x in data: 
        tree.insert(x)
        
    tree.inorderTraversal(tree.root)

testBinarySearchTree()

    