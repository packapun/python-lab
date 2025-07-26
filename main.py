from typing import List 

"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent 
the start and the end of the ith interval and intervals is sorted in ascending order by starti. 
You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending 
order by starti and intervals still does not have any overlapping intervals 
(merge overlapping intervals if necessary).

Return intervals after the insertion.

Note that you don't need to modify intervals in-place. You can make a new array and return it.
Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


"""
Approach 
1. Initialize a new output array which will contain the final interval list 
2. Loop through the given interaval list 
3. If the end of the current interval is less than the start of the new interval, add it to the output
else mark this as the start of a new interval to insert starting the smallest start value 
4. Proceed to the next intervals. Keep moving till the current interval's end is less than to the end of the new interval. 
Use the max end value between the current interval and the new interval 
5. Add the remaining intervals to the output
Time : O(n)
Space : O(n)
"""



"""
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""

def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
    if not intervals or not newInterval:
        return intervals 
    
    output = []
    index = 0
    n = len(intervals)
    new_start = newInterval[0] # 4
    new_end = newInterval[1] # 8
    
    while index < n:
        curr_start = intervals[index][0] #3
        curr_end = intervals[index][1] #5
        if curr_end < new_start or curr_start > new_end: # 5 < 4 or 3 > 8
            output.append(intervals[index]) # [[1,2]]
            index += 1
        else:
            # Extract start
            start = min(new_start, curr_start) # 3
            while curr_end < new_end and index < n: # 10 < 8
                index += 1
                curr_start = intervals[index][0]
                curr_end = intervals[index][1]
            
            # Extract the end 
            if curr_start <= new_end:
                end = max(curr_end,new_end) # max(10,8) = 10
                index += 1
            else:
                end = new_end 
            output.append([start,end]) # [3,10]
        
    return output


def test_insert_interval():
    intervals = [[1,3],[6,9]]
    new_interval = [2,5]
    ret = insert(intervals,new_interval)
    print(ret)


    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    new_interval = [4,8]
    ret = insert(intervals,new_interval)
    print(ret)

test_insert_interval()


# TTS (time to solve) : 30min


# ===========
def lengthOfLongestSubstring(self, s: str) -> int:
    max_length = 0
    left = right = 0
    seen = {}
    while right < len(s):
        if s[right] not in seen:
            # Unseen character
            seen[s[right]] = right  # a:0
        else:
            # We've seen this character 
            prev_index = seen[s[right]] # 0
            if prev_index >= left: 
                left = prev_index + 1
            seen[s[right]] = right 
        
        max_length = max(max_length, right - left + 1)
        right += 1
    return max_length 

# TTS : 20min


# ===============

def longestOnes(self, nums: List[int], k: int) -> int:
    zero_count = 0
    left = right = 0
    max_count = 0 
    
    while right < len(nums):
        if nums[right] == 0:
            zero_count += 1 #3
            while zero_count > k:
                if nums[left] != 0:
                    left += 1
                else:
                    zero_count -= 1
                    left += 1

        max_count = max(max_count, right - left + 1) #1
        right += 1
    return max_count

# TTS : 10:42min
