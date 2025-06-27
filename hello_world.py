import math

def mergeSort(arr): 
    n = len(arr)
    if n < 2:
        return arr
    mergeUtil(0, n-1, arr)
    return arr

def mergeUtil(l, r, arr):
    if l < r:
        m = (l + r) // 2  # Standard midpoint calculation
        mergeUtil(l, m, arr)      # Left half: [l, m]
        mergeUtil(m + 1, r, arr)  # Right half: [m+1, r]
        mergeRoutine(l, m, r, arr)

def mergeRoutine(l, m, r, arr):
    # Create temporary arrays for left and right subarrays
    leftArray = arr[l:m+1]    # [l, m] inclusive
    rightArray = arr[m+1:r+1] # [m+1, r] inclusive
    
    i = j = 0
    k = l  # Start merging back into original array at position l
    
    # Merge the two arrays
    while i < len(leftArray) and j < len(rightArray):
        if leftArray[i] <= rightArray[j]:
            arr[k] = leftArray[i]
            i += 1
        else:
            arr[k] = rightArray[j]
            j += 1
        k += 1
    
    # Copy remaining elements
    while i < len(leftArray):
        arr[k] = leftArray[i]
        i += 1
        k += 1
    
    while j < len(rightArray):
        arr[k] = rightArray[j]
        j += 1
        k += 1


def selectionSort(arr):
    # Find the smallest element and move it to the end of the sorted boundary 
    n = len(arr) 
    
    # Check for the base case 
    if n < 2:
        return arr
    
    for i in range(n-1):
        minIndex = i 

        for j in range(i+1,n):
            if arr[j] < arr[minIndex]:
                minIndex = j 
        
        if minIndex != i:
            arr[i],arr[minIndex] = arr[minIndex],arr[i]



def insertionSort(a): 
    n = len(a)
    if n < 2:
        return a  # Return the array for consistency
    
    for j in range(1, n):  # j is the current element to insert
        curr = a[j]
        k = j - 1  # Start comparing from the previous element
        
        while k >= 0 and a[k] > curr:
            a[k + 1] = a[k]
            k -= 1
        
        a[k + 1] = curr
    return a

# O(n^2)
def bubble_sort(a): 
    n = len(a)
    print(a,n)
    for i in range(0,n):
        for j in range(0,n-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
        print(a)

# O(n*log(n))
"""
1. Decide on a pivot
2. Move all elements less than the pivot to the left of the pivot 
3. Move all element greater than the pivot to the right of the pivot 
4. Repeat 1-3 for the left and right subarrays

[5,4,3,12,1,7]
[5,4,3,1,12,7]
"""
def quicksort(arr):
    n = len(arr)
    if n < 2:
        return arr
    quicksortUtil(arr,0,n-1)
    

def quicksortUtil(arr,l,r):
    if l < r:
        pivotIndex = partition(arr, l, r)
        quicksortUtil(arr, l, pivotIndex-1)
        quicksortUtil(arr, pivotIndex+1, r)
            
            
def partition(arr,l,r):
    pivot = arr[r]    

    i = l - 1

    for j in range(l,r):
        if arr[j] <= pivot:
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
    
    arr[i+1],arr[r] = arr[r],arr[i+1]
    return i + 1
        
        

# Main Driver function
a = [6,5,4,3,2,1]
quicksort(a)
print(a)
