def heapify(arr, heap_size, root_index):
    largest = root_index
    left = 2*root_index + 1
    right = 2*root_index + 2

    print(f"Heapifying subtree rooted at index {root_index} (value: {arr[root_index]})")

    if left < heap_size and arr[left] > arr[largest]:
        largest = left 
        print(f"  Left child {arr[left]} > current largest {arr[root_index]}")
    
    if right < heap_size and arr[right] > arr[largest]:
        largest = right 
        print(f"  Right child {arr[right]} > current largest")

    if largest != root_index: 
        arr[root_index],arr[largest] = arr[largest], arr[root_index]
        print(f"  Swapped: {arr}")
        heapify(arr,heap_size, largest)     
    else:
        print(f"  No swap needed, heap property satisfied")


def heapsort(a):
    n = len(a)
    for i in range(int(n/2)-1,-1,-1):
        heapify(a,n,i)

    for i in range(n-1, -1, -1):
        a[0],a[i] = a[i],a[0]
        heapify(a,i,0)
        

    

heap = [4, 10, 3, 5, 1]
heapsort(heap)
print(heap)