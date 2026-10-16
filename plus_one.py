# Sivabalan M, BE ECE, Day 16
# Problem: Add one to the integer represented by a list of digits.

class Solution:
    def plusOne(self, digits):
        # Process digits from right to left, starting with the ones place.
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # A 9 becomes 0, and the carry moves to the digit on the left.
            digits[i] = 0

        # If every digit was 9, add a new leading 1.
        return [1] + digits


if __name__ == "__main__":
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))  # [1, 2, 4]
    print(solution.plusOne([9, 9, 9]))  # [1, 0, 0, 0]
