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