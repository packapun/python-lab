from typing import List 

def mergesort(nums:List[int]):
    if not nums:
        return 
    l = 0 
    r = len(nums)-1
    mergesort_util(nums,l,r)
    
    
def mergesort_util(nums,l,r):
    if l < r:
        mid = (l+r)//2
        mergesort_util(nums,l,mid)
        mergesort_util(nums,mid+1,r)
        merge(nums,l,r,mid)
        


def merge(arr,l,r,mid):
    left = arr[l:mid+1]
    right = arr[mid+1:r+1]
    i = j = 0
    k = l 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1

def test_mergesort():
    nums = [5,4,3,2,1]
    mergesort(nums)
    print(nums)

test_mergesort()