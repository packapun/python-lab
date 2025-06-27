print('Hello world')


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

a = [6,5,4,3,2,1]
insertionSort(a)
