from typing import List
# TwoSum problem 
def twoSum(nums:List[int], target:int) -> List[int]:
    if not nums:
        return []   
    sorted_nums = sorted(nums)
    left = 0
    right = len(nums)-1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum < target:
            left += 1
        elif current_sum > target:
            right -= 1
        else:
            return [left,right]
    return []




# Test case
def test_twosum():
    nums = [5,2,1,7]
    target = 12
    assert twoSum(nums,target) == [0,3]

test_twosum()

