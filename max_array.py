def find_max(arr):
    maximum = arr[0]  # Assume first element is the max
    for i in range(1, len(arr)):
        if arr[i] > maximum:
            maximum = arr[i]
    return maximum

arr = [1, 2, 34, 5]
print(find_max(arr))  # Output: 34
