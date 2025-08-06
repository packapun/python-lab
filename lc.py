from typing import List, Optional
from collections import Counter,defaultdict
from heapq import heappush, heappop, heapify

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

def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        mapping = {
            '2': 'abc',
            '3': 'def', 
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []
        def backtrack(index, current):
            if index == len(digits):
                result.append(current)
                return 
            digit = digits[index]
            letters = mapping[digit]
            for letter in letters:
                backtrack(index+1, current+letter)

        backtrack(0,"")
        return result        

def compress(chars):
    """
    Compress string in-place using consecutive character counting.
    
    Args:
        chars: List of characters to compress
    
    Returns:
        int: New length of the compressed array
    """
    if not chars:
        return 0
    
    # Two pointers: read for reading, write for writing
    read = 0
    write = 0
    
    while read < len(chars):
        current_char = chars[read]
        count = 1
        
        # Count consecutive occurrences of current character
        while read + count < len(chars) and chars[read + count] == current_char:
            count += 1
        
        # Write the character
        chars[write] = current_char
        write += 1
        
        # If count > 1, write the count as string characters
        if count > 1:
            count_str = str(count)
            for digit in count_str:
                chars[write] = digit
                write += 1
        
        # Move read pointer to next group
        read += count
    
    return write


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0
        
    number_set = set()
    seq_length = 0
    max_length = 0
    number_set = set(nums)

    for x in nums:
        if x not in number_set:
                continue
        # print("Processing {}".format(x))
        number_set.remove(x)
        seq_length = 1
        i = x + 1
    
        while i in number_set:
            # print("Looking for {}".format(i))
            # print(number_set, seq_length)
            seq_length += 1
            number_set.remove(i)
            i = i+1
            
        i = x - 1
        while i in number_set:
            # print("Looking for {}".format(i))
            # print(number_set, seq_length)
            seq_length += 1
            number_set.remove(i)
            i = i-1
        # print("Max length = {}".format(max_length))
        max_length = max(max_length, seq_length)
    return max_length
    

    
    
    

"""
## LC 1152
VisitEvent(timestamp, username, website_id)
username = [aamir,aamir,aamir,azhar...]
timestamp = [1,2,3,4...]
website = [a,b,c,a...]

Find the pattern which occurs the most across all users
aamir -> a,b,c
david -> a,b,c

Pattern : abc 

Simple approach: 
1. Find all the 3-website patterns for each user
2. For each pattern, keep a counter 
3. increment the counter as users visit websites
4. return the pattern with the highest count


aamir -> a,b,c,d
Patterns : abc,bcd,acd,abd

[
aamir:abcdaadd,
azhar:aaaabbbb
]

[abc:3,bcd:2,acd:1,abd:1]

"""
def most_visited_pattern(self, usernames:List[str], websites:List[int], timestamps:List[int]) -> List[str]:
    users_visits = defaultdict(list)

    for user, _, site in sorted(zip(usernames,timestamps,websites), key=lambda x:x[1]):
        users_visits[user].append(site)
    patterns_count = Counter()
    for sites in users_visits.values():
        number_of_sites = len(sites)
        unique_patterns = set()
        if number_of_sites > 2:
            for i in range(number_of_sites-2):
                for j in range(i+1,number_of_sites-1):
                    for k in range(j+1,number_of_sites):
                        unique_patterns.add((sites[i],sites[j],sites[k]))
        
        for pattern in unique_patterns:
            patterns_count[pattern] += 1
        
    return sorted(patterns_count.items(), key=lambda x:(-x[1],x[0]))[0][0]


def print_permutations(s:str):
    def permute(chars,start=0):
        if start == len(chars):
            print(''.join(chars))
        for i in range(start, len(chars)):
            chars[start],chars[i] = chars[i],chars[start]
            permute(chars,i+1)
            chars[start],chars[i] = chars[i],chars[start]
    
    permute(list(s))
    print()


# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# O(n*m). KMP is better
def strStr(self, haystack: str, needle: str) -> int:
    if not haystack or not needle:
        return -1
    start = needle[0]
    for i in range(0,len(haystack)):
        current_char = haystack[i]
        if current_char == start:
            j = 1
            while (i+j) < len(haystack) and j < len(needle):
                if haystack[i+j] == needle[j]:
                    j += 1
                else:
                    break
            if j == len(needle):
                return i
    return -1

def gcdOfStrings(self, str1: str, str2: str) -> str:
    m, n = len(str1), len(str2)
    
    if m == 0 or n == 0:
        return ""
    
    gcd_len = math.gcd(m, n)
    candidate = str1[:gcd_len]  # Always use str1 as source
    
    # Check if candidate can construct both strings
    if (candidate * (m // gcd_len) == str1 and 
        candidate * (n // gcd_len) == str2):
        return candidate
    
    return ""

def threeSum(self, nums: List[int]) -> List[List[int]]:
    if not nums or len(nums) < 3 :
        return []
    n = len(nums)
    nums.sort()
    output = []
    print(nums)
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        if nums[i] > 0:
            break 
        
        left = i+1
        right = n-1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum == 0:
                output.append([nums[i], nums[left], nums[right]])
                
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif current_sum > 0:
                right -= 1
            else:
                left += 1
    return output



# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """
        Time Complexity: O(n log n)
        Space Complexity: O(log n)
        """
        if not head:
            return None
        
        if not head.next:
            return TreeNode(head.val)

        slow = fast = head
        prev = None 
        while fast and fast.next:
            prev = slow 
            slow = slow.next
            fast = fast.next.next 

        if prev:
            prev.next = None 

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head if prev else None)
        root.right = self.sortedListToBST(slow.next)
        return root

# LC 1094
def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_location = max(trip[2] for trip in trips)
        diff = [0] * (max_location + 1)
        for passengers, start, end in trips:
            diff[start] += passengers
            diff[end] -= passengers
        current_passengers = 0 
        for change in diff:
            current_passengers += change 
            if current_passengers > capacity:
                return False 
        return True


# LC 958
def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root])
        found_null = False
        while queue:
            node = queue.popleft()
            
            if node is None:
                found_null = True
            else:
                if found_null:
                    return False
                queue.append(node.left)
                queue.append(node.right)
        return True

# LC 91
def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)

        dp = [0]*(n+1)

        # Base cases
        dp[0] = 1 # Empty String
        dp[1] = 1 # First character 

        for i in range(2,n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        return dp[n]


# LC 238
def productExceptSelf(self, nums: List[int]) -> List[int]:
    if not nums:
        return []
    n = len(nums)
    prefix = [1]*(n)
    suffix = [1]*(n)

    for i in range(1,n):
        prefix[i] = prefix[i-1]*nums[i-1]

    for i in range(n-2,-1,-1):
        suffix[i] = suffix[i+1]*nums[i+1]
    
    output = []
    for i in range(n):
        output.append(prefix[i]*suffix[i])
    return output


# LC 1882 

def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
    n, m = len(servers), len(tasks)

    # min-heap of available servers on the basis of weight 
    available = [(servers[i],i) for i in range(n)]
    heapq.heapify(available)

    # min-heap of busy servers based on free_time 
    busy = []
    result = []
    current_time = 0

    for task_idx in range(m):
        current_time = max(current_time, task_idx)
        while busy and busy[0][0] <= current_time:
            free_time,weight,server_idx = heapq.heappop(busy)
            heapq.heappush(available, (weight,server_idx))

        if not available:
            free_time,weight,server_idx = heapq.heappop(busy)
            current_time = free_time 
            heapq.heappush(available, (weight,server_idx))
        
            while busy and busy[0][0] <= current_time:
                free_time,weight,server_idx = heapq.heappop(busy)
                heapq.heappush(available, (weight,server_idx))

        weight, server_idx = heapq.heappop(available)
        result.append(server_idx)

        task_duration = tasks[task_idx]
        heapq.heappush(busy, (current_time + task_duration, weight, server_idx))
    
    return result
