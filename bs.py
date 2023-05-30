import random
arr = random.sample(range(1, 100), 10)
n = len(arr)

for i in range(0, n):
    curr_element = arr[i]
    j = i - 1
    while j >= 0 and curr_element < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = curr_element

print(arr)
