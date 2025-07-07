import heapq
from typing import List
from collections import Counter

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.


# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.



"""
Naive approach = O(k*len(nums))

Better approach = O(nlogn)
Heap: 

ExtractMin -> O(1)
Heapify -> O(log(n))

k*log(n)
"""

def findKMostFrequent(input:List[int], k:int) -> List[int]:
    if not input:
        return []
    # Initialize variables
    output = []
    heap = []
    c = Counter(input)    

    for key,value in c.items():
        heapq.heappush(heap, (-value,key))
    print(heap)
    
    if k >= len(heap):
        return [x[1] for x in heap]

    for i in range(0,k):
        value,key = heapq.heappop(heap)
        output.append(key)
    return output


nums = [1,1,1,2,2,3,3,3,3,3,3,4,4,4,4,6,6,6,6,6,6,6,6,6]
k = 30
print(findKMostFrequent(nums,k))

