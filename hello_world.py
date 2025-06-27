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


def twoSum(nums, target: int) -> int:
    hashMap = dict()
    for i, num in enumerate(nums):
        complement = target-num
        if complement in hashMap:
            return [i, hashMap[complement]]
        else:
            hashMap[nums[i]] = i 
    return []



def isAnagram(s: str, t: str) -> bool:
    # sorted(s) == sorted(t)
    if len(s) != len(t):
        return False
    hashMap = dict() 
    for x in s: 
        if x in hashMap:
            hashMap[x] += 1
        else:
            hashMap[x] = 1 
    print(hashMap)

    for x in t: 
        if x not in hashMap:
            return False
        else:
            hashMap[x] -= 1
            if hashMap[x] == 0:
                del hashMap[x]

    print(hashMap)
    return len(hashMap) == 0


isAnagram = isAnagram('aamir','rimaa')
print(isAnagram)


# Practice these until you can write them quickly:

# 1. Character frequency counter
def char_count(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    return count

# 2. Two sum pattern
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

# 3. Sliding window template
def sliding_window(arr, k):
    # Pattern for fixed-size window problems
    pass