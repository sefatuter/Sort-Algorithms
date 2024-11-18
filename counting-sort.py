import random
import time

# Best: O(n+k)
# Wors: O(n+k)
# Stable:   ⛔
# Inplace:  ⛔

def CountingSort(input_array):
    M = max(input_array)     # Finding the maximum element of input_array.

    count_array = [0] * (M + 1)  # Initializing count_array with 0

    for num in input_array:     # Mapping each element of input_array as an index of count_array
        count_array[num] += 1

    for i in range(1, M + 1):   # Calculating prefix sum at every index of count_array
        count_array[i] += count_array[i - 1]

    output_array = [0] * len(input_array)

    for i in range(len(input_array) - 1, -1, -1):
        output_array[count_array[input_array[i]] - 1] = input_array[i]
        count_array[input_array[i]] -= 1

    return output_array


n = 1000000
arr = []

for i in range(n):
    arr.append(random.randint(1, 100000))

start_time = time.time()

arr = CountingSort(arr)

end_time = time.time()
time_taken = end_time - start_time

for val in arr:
    print(val, end=" ")
    
print(f"\n\nCounting Sort took {time_taken:.6f} seconds to sort the array.")