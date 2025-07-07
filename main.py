from typing import List
from collections import Counter

def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0
        
    number_set = set()
    seq_length = 0
    max_length = 0
    
    for x in nums:
        number_set.add(x)

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
    

input = [0]
print(longestConsecutive(input))
