def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]  # swap
        start += 1
        end -= 1

    return arr
arr = [14,2,43,4,5]
print(reverse_array(arr))