def find_min(arr):
    minimun = arr[0]  # Assume first element is the max
    for i in range(1, len(arr)):
        if arr[i] < minimun:
            minimun = arr[i]
    return minimun

arr = [1, 2, 34, 5]
print(find_min(arr))  # Output: 34
