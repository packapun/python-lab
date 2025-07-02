from heapq import heappush, heappop
from collections import Counter
def isValid(self, s: str) -> bool:
    bracketMap = {'}': '{', ')': '(', ']': '['}
    stack = []
    
    for char in s:
        if char in bracketMap:  # closing bracket
            if not stack or stack.pop() != bracketMap[char]:
                return False
        elif char in '{([':  # opening bracket
            stack.append(char)
        # ignore non-bracket characters (if any)
    
    return len(stack) == 0


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


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_groups = {}
    for string in strs: 
        key = str(sorted(string))
        if key in anagram_groups:
            anagram_groups[key] += [string]
        else:
            anagram_groups[key] = [string]
    return list(anagram_groups.values())


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = [] 
        c = Counter(nums)
        for c,v in c.items():
            heappush(h,(-v,c))
        output = []
        for i in range(0,k):
            output += [heappop(h)[1]]
        return output

def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        char_index = {}
        left = 0 
        max_length = 0 
        current_length = 0 
        for right in range(len(s)):
            char = s[right]
            if char in char_index and char_index[char] >= left:
                left = char_index[char]+1
            char_index[char] = right 
            current_length = right - left + 1 
            if current_length > max_length:
                max_length = current_length 
        return max(current_length, max_length)


def longestOnes(self, nums: List[int], k: int) -> int:
    if not nums:
        return 0
    max_size = 0 
    left = 0 
    zero_count = 0 
    for right in range(len(nums)):
        digit = nums[right]
        if digit == 0:
            zero_count += 1
            
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_size = max(max_size, right - left + 1)
    return max_size 

"""
https://leetcode.com/problems/insert-interval/description/
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
"""

def insert(intervals: [[int]], newInterval: [int]) -> [[int]]:
    if not intervals or not intervals[0]:
        return []
    result = []
    i = 0
    s,t = newInterval[0],newInterval[1]
    n = len(intervals)

    while i < n and intervals[i][1] < s:
        result.append(intervals[i])
        i += 1

    start = newInterval[0]
    end = newInterval[1]

    while i < n and intervals[i][0] <= end:
        start = min(start,intervals[i][0])
        end = max(end, intervals[[i][1]])
        i += 1
    
    result.append([start,end])

    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

def subsets(self, nums: List[int]) -> List[List[int]]:
    result = []
    def backtrack(start, current_subset):
        result.append(current_subset[:])
        for i in range(start, len(nums)):
            current_subset.append(nums[i])
            backtrack(i+1, current_subset)
            current_subset.pop()

    backtrack(0,[])
    return result
        

