from typing import List
"""
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

"""

"""
[0,0,0,0,0]
Output: 0
You need at least one 1

Sliding window 

[0,1,1,1,0]
k = 1
budget = 1
max_count = max(max_count,curr_count)


Approach:
1. Keep two pointers, left and right and start at index 0,1
2. If the current element is 1, move right 
3. If the current element is 0, shift left if no flips left, else flip and move right 
4. After every shift, check max_count
5. Maintain a variable which keeps track of how many zeroes have been flipped

max = right - left + 1

[1,1,0,0,0,1,1,1,1,1,1]
k = 1

left = right 
budget = k 
"""

def longestOnes(nums:List[int], k:int) -> int:
    if not nums:
        return 0    
    zero_count = 0 
    left = 0
    max_size = 0
    for right in range(0,len(nums)):
        digit = nums[right]
        if digit == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_size = max(max_size, right - left + 1)
    return max_size



# Test 
input = [9,1,4,7,3,-1,0,5,8,-1,6]
k = 2
print(longestOnes(input,k))





