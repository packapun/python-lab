from typing import List

# TwoSum [x]
# isPalindrome[x]
# longestPrefix[x]
# isValid[x]
# reverseLL [x]
# majorityElement[x]
# Stack [ ]
# Queue  using [ ]
# LinkedList [ ]
# Mergesort [ ]
# Quicksort[ ]

def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False 
    if x < 10:
        return True

    reversed_num = 0
    num = x 
    while num > 0:
        remainder = int(num%10) 
        reversed_num = reversed_num*10 + remainder 
        num = num//10 
        # print("reminder = {}, reversed_num = {}, num = {}".format(remainder, reversed_num, num))
    # print("Comparing {} and {}".format(reversed_num, x))
    return reversed_num == x
        

# Two Sum 
def twoSum(nums:List[int], target:int) -> List[int]:
    if not nums:
        return []
    hash_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in hash_map:
            return [hash_map[complement], i]
        else:
            hash_map[num] = i  
    return []

# Longest prefix 

def longestCommonPrefix(self, strs: List[str]) -> str:
    if not strs:
        return ""
    candidate = strs[0]
    longest_prefix = ""
    for i in range(len(candidate)):
        letter = candidate[i]
        for string in strs:
            if i >= len(string) or string[i] != letter:
                    return longest_prefix
        longest_prefix += letter
    return longest_prefix


def isValid(self, s: str) -> bool:
    if not s:
        return False
    mapping = {'}':'{', ']':'[', ')':'('}
    stack = []

    for char in s:
        if char in mapping:
            # closing bracket
            if len(stack) == 0 :
                return False 
            top = stack.pop()
            if top != mapping[char]:
                return False 
        else:
            # opening bracket
            stack.append(char)
    return len(stack) == 0


def majorityElement(self, nums: List[int]) -> int:
    if not nums:
        return 0
    votes = 1
    element = nums[0] 
    for i in range(1,len(nums)):
        x = nums[i]
        if x == element:
            votes += 1
        else:
            votes -= 1
            if votes == 0:
                element = x 
                votes = 1 
    return element


def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return head

    new_head = self.reverseList(head.next)
    head.next.next = head
    head.next = None
    return new_head


nums = [4,6,1,2]
target = 8 
ret = twoSum(nums, target)
print(ret)



# ====
def maxArea(self, height: List[int]) -> int:
    if not height:
        return 0

    n = len(height)
    left = 0
    right = n-1
    max_area = 0 
    while left < right:
        curr_area = (right - left)*min(height[left], height[right])
        max_area = max(max_area, curr_area)
        if height[left] < height[right]:
            # Move left 
            left += 1
        else:
            # Move right
            right -= 1
    return max_area

# TTS : <=5min

# ===