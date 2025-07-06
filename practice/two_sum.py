from typing import List, Optional, Tuple
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

"""
Simple example 

input = [1,3,5,7,9]
target = 4

output = [0,1]

Assumptions:
1. Can we have negative numbers? Yes
2. What's the input size? 10*4
3. Can we have decimals or floating point? Keep it simple and assume integer

Simple approach:
1. Find all the pairs which should be O(n^2)
2. If the pair adds up to target, return it


Better approach:
1. Use a hashmap to create a mapping between value and index 
2. Iterate through the elements 
3. If target - curr_element exists, return current index and index of the complement 
Note - We are assuming that there must exist a solution in the array 
"""

def twoSum(input:List[int], target:int) -> Optional[Tuple[int,int]]:
    if not input:
        return None
    index_map = {}
    for i in range(0,len(input)):
        num = input[i]
        complement = target - num 
        if complement in index_map:
            return (index_map[complement],i)
        else:
            index_map[num] = i
    return None
            


# Test 
input = [1,3,5,7]
target = 12
print(twoSum(input,target))


