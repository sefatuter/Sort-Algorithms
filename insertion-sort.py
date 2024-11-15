import random
import time

def InsertionSort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i - 1 # Compared one
        while (j >= 0 and arr[j] > tmp):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp


n = 100000
arr = []

for i in range(n):
    arr.append(random.randint(1, 1000))

start_time = time.time()

InsertionSort(arr)

end_time = time.time()
time_taken = end_time - start_time

for val in arr:
    print(val, end=" ")
    
print(f"\n\nInsertion Sort took {time_taken:.6f} seconds to sort the array.")
