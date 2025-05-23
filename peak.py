class Solution(object):
    def peak_value(self, lst):
        low = 0
        high = len(lst) - 1

        while low <= high:
            mid = (low + high) // 2

            # Safe checks for peak
            if (mid == 0 or lst[mid] >= lst[mid - 1]) and (mid == len(lst) - 1 or lst[mid] >= lst[mid + 1]):
                return lst[mid]  # main line TP(turning point)

            # If left neighbor is greater, move left
            elif mid > 0 and lst[mid - 1] > lst[mid]:
                high = mid - 1
            else:
                low = mid + 1

        return -1  # Shouldn't reach here if input is valid

# Example usage
solution = Solution()
arr = [1, 3, 20, 30, 1, 0]
print("The peak is:", solution.peak_value(arr))
