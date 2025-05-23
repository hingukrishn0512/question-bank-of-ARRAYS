def count_even(l1):
    count = 0
    for num in l1:
        if num % 2 == 0:
            count += 1
    return count

l1 = [1, 2, 4, 6, 8, 10]
print(f"Total numbers: {len(l1)}")
print(f"Even numbers in the list: {count_even(l1)}")
