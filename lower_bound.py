class Solution:
    def lowerBound(self, arr, target):
        i = 0
        j = len(arr)

        while i < j:
            mid = (i + j) // 2

            if arr[mid] >= target:
                j = mid
            else:
                i = mid + 1

        return i
