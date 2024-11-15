import random
import time

def heapify(arr, n, i):
    largest = i 
    
    #  left index = 2*i + 1
    l = 2 * i + 1 
    
    # right index = 2*i + 2
    r = 2 * i + 2  

    # If left child is larger than root
    if l < n and arr[l] > arr[largest]:
        largest = l

    # If right child is larger than largest so far
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap

        # Recursively heapify the affected sub-tree
        heapify(arr, n, largest)

# Main function to do heap sort
def HeapSort(arr):
    
    n = len(arr) 

    # Build heap (rearrange array)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract an element from heap
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] 
        heapify(arr, i, 0)
        
        
n = 1000000
arr = []

for i in range(n):
    arr.append(random.randint(1, 1000))

start_time = time.time()

HeapSort(arr)

end_time = time.time()
time_taken = end_time - start_time

for val in arr:
    print(val, end=" ")
    
print(f"\n\nHeap Sort took {time_taken:.6f} seconds to sort the array.")