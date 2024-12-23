import random
import time

# Best: O(n+2ᵏ)
# Wors: O(n+2ᵏ)
# Stable:   ✅
# Inplace:  ⛔

def PigeonholeSort(arr):
    min_val = min(arr)
    max_val = max(arr)
    
    size = max_val - min_val + 1 # find Range
    
    holes = [0] * size 
    
    for num in arr:
        holes[num - min_val] += 1 # increase holes accordingly numbers we have
    # print(holes)
    sorted_arr = []
    for index, count in enumerate(holes):
        sorted_arr.extend([index + min_val] * count)
    
    return sorted_arr


n = 10
arr = []

for i in range(n):
    arr.append(random.randint(1, 10))

start_time = time.time()

arr = PigeonholeSort(arr)

end_time = time.time()
time_taken = end_time - start_time

for val in arr:
    print(val, end=" ")
    
print(f"\n\nPigeonhole Sort took {time_taken:.6f} seconds to sort the array.")