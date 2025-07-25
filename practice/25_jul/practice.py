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