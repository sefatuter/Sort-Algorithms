import random
import time

# Best: O(nlogn)
# Wors: O(n²)
# Stable:   ⛔
# Inplace:  ✅

def QuickSort(a, low, high):
    if low < high:
        pivot = a[low]  # Select Pivot low
        i, j = low + 1, high
        while True:
            while i <= j and a[i] < pivot: i += 1
            while i <= j and a[j] > pivot: j -= 1
            if i <= j:
                a[i], a[j] = a[j], a[i]
                i, j = i + 1, j - 1
            else:
                break
        a[low], a[j] = a[j], a[low]  # Swap pivot with a[j]
        QuickSort(a, low, j - 1)  # Recur for left
        QuickSort(a, j + 1, high)  # Recur for right


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
