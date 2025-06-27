# 1. Character frequency counter
def char_count(s):
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    return count

# 2. Two sum pattern
def two_sum(nums, target):
    seen = {}
    for i, num in enumerate(nums):
        if target - num in seen:
            return [seen[target - num], i]
        seen[num] = i

# 3. Sliding window template
def sliding_window(arr, k):
    # Pattern for fixed-size window problems
    pass