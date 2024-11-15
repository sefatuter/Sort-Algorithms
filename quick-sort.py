import random
import time


def QuickSort(a, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(a, low, high)
        # Recursively sort the left and right subarrays
        QuickSort(a, low, pivot_index - 1)
        QuickSort(a, pivot_index + 1, high)

def partition(a, low, high):
    pivot = a[low]  # Choose the pivot element
    i = low + 1
    j = high

    while True:
        # Move i to the right as long as a[i] < pivot
        while i <= j and a[i] < pivot:
            i += 1
        # Move j to the left as long as a[j] > pivot
        while i <= j and a[j] > pivot:
            j -= 1
        if i <= j:
            # Swap elements at i and j
            a[i], a[j] = a[j], a[i]
            i += 1
            j -= 1
        else:
            break

    # Swap the pivot element with a[j]
    a[low], a[j] = a[j], a[low]
    return j  # Return the pivot index


n = 1000000
arr = []

for i in range(n):
    arr.append(random.randint(1, 1000))

start_time = time.time()

QuickSort(arr, 0, len(arr) - 1)

end_time = time.time()
time_taken = end_time - start_time

for val in arr:
    print(val, end=" ") 
    
print(f"\n\nQuic Sort took {time_taken:.6f} seconds to sort the array.")
