import random
import time

def SelectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
      
        min_idx = i
        
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
              
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]


n = 1000000
arr = []

for i in range(n):
    arr.append(random.randint(1, 1000))

start_time = time.time()

SelectionSort(arr)

end_time = time.time()
time_taken = end_time - start_time

for val in arr:
    print(val, end=" ")
    
print(f"\n\nSelection Sort took {time_taken:.6f} seconds to sort the array.")