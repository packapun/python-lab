# LC Practice 25th July

# Selection sort 

"""
What does this algorithm do? 
1. Find the smallest element in the unsorted portion 
2. Add this element to the sorted portion of the list 
3. Do this till all elements are inside the sorted portion 
"""
from typing import List 

# Sorts an array in O(n^2) time 
def selection_sort(nums:List[int]):
    i = -1 
    n = len(nums) # 5

    while i < n-1:
        min_value = nums[i+1] # 5
        min_index = i+1 # 0
        
        for j in range(i+2, n):
            if nums[j] < min_value: # 4 < 5
                min_value = nums[j] # 1
                min_index = j  # 4

        i += 1 # 0
        nums[min_index],nums[i] = nums[i], nums[min_index] # swap index 0 and 4
    print(f"Final sorted version {nums}")
        

# Test selection sort
def test_selection_sort():
    nums = [5,4,3,2,1]
    selection_sort(nums)
    assert nums == [1,2,3,4,5]
    print("test case passed")


test_selection_sort()

#------------------------------------


# Implement Quick Sort
"""
Algorithm:
1. Choose a pivot element
2. Move all elements less than the pivot to the left
3. Move all element greater than the pivot to the right 
4. Swap the pivot to the index between these two sections 
5. Repeat for the left and right sections 

Time : O(n*logn)
Space : O(logn)
"""

def quicksort(nums:List[int], l , r):
    if l < r:
        mid = partition(nums,l,r)
        quicksort(nums,l,mid-1)
        quicksort(nums,mid+1,r)
     
def partition(nums, l, r):
    pivot_index = r
    pivot = nums[r]
    i = l
    for k in range(l,r):
        if nums[k] < pivot:
            nums[k],nums[i] = nums[i],nums[k]
            i += 1
    nums[pivot_index],nums[i] = nums[i],nums[pivot_index]
    print("Partition output : {}".format(nums[l:r+1]))
    return i
    

def test_quicksort():
     nums = [5,4,3,2,1]
     quicksort(nums, 0, len(nums)-1)
     print("testcase:quicksort output {}".format(nums))
     assert nums == [1,2,3,4,5]

def test_partition():
    nums = [1,2,3,4,5]
    index = partition(nums,0,len(nums)-1)
    assert index == 4
    assert nums == [1,2,3,4,5]
    
    nums = [5,4,3,2,1]
    index = partition(nums,0,len(nums)-1)
    assert index == 0
    assert nums == [1,4,3,2,5]
    

def test_suite():
    test_partition()
    test_quicksort()

test_suite()

# TOS (time to solution) : 16m37s
#  ---------- 


def mergesort(nums:List[int], left, right):
    if left < right:
        mid = (left + right)//2
        mergesort(nums,left, mid)
        mergesort(nums,mid+1, right)
        merge(nums,left,mid,right)
        

def merge(nums:List[int], left:int, mid:int, right:int):
    left_subarray = nums[left:mid+1]
    right_subarray = nums[mid+1:right+1]
    k = left 
    i = 0 
    j = 0 
    while i<len(left_subarray) and j<len(right_subarray):
        if left_subarray[i] < right_subarray[j]:
            nums[k] = left_subarray[i]
            i += 1
        else:
            nums[k] = right_subarray[j]
            j += 1
        k += 1

    while i < len(left_subarray):
            nums[k] = left_subarray[i]
            i += 1
            k += 1

    while j < len(right_subarray):
            nums[k] = right_subarray[j]
            j += 1
            k += 1


# =======
"""
Problem Statement:
Implement the following class:

MovingAverage(int size): Initializes with the window size.

double next(int val): Adds val to the stream and returns the moving average of the last size values.

If there are fewer than size values in the stream so far, return the average over the values present.

MovingAverage movingAverage = new MovingAverage(3);
movingAverage.next(1);   // returns 1.0
movingAverage.next(10);  // returns 5.5
movingAverage.next(3);   // returns 4.66667
movingAverage.next(5);   // returns 6.0

"""
from collections import deque

class MovingAverage: 
    def __init__(self,window_size:int):
        self.window_size = window_size 
        self._count = 0
        self._sum = 0
        self.storage = deque()


    def next(self,value:int) -> float:
        # Add value to collection 
        if self._count < self.window_size:
            self.storage.append(value)
            self._count += 1
        else: 
            x = self.storage.popleft()
            self._sum -= x
            self.storage.append(value)
        
        self._sum += value 
        print("storage : {}".format(self.storage))
        
        # Return the average 
        average = self.calculate_average(self._sum, self._count)
        print("average : {}".format(sum))
        return average

    

def test_moving_average():
    window_size = 3
    mov_average = MovingAverage(window_size)
    assert mov_average.next(1) == 1.0
    assert mov_average.next(10) == 5.5
    assert mov_average.next(3) == 4.666666666666667
    assert mov_average.next(5) == 6.0
    

def test_calculatesum():
    pass 

def test_suite():
    test_calculatesum()
    test_moving_average()

test_suite()

# TOS : 15min 
# ===========

# Invert given binary tree
def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None
    root.left,root.right = root.right,root.left
    root.left = self.invertTree(root.left)
    root.right = self.invertTree(root.right)
    return root


# ==========
def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    counter = Counter(magazine)
    for char in ransomNote:
        if char not in counter or counter[char] == 0:
            return False 
        counter[char] -= 1
    return True



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