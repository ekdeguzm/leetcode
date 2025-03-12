from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)

        i = length - 1

        for i in range(length - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits


solution = Solution()

digits = [1, 2, 9, 9]

result = solution.plusOne(digits)

print(result)

print(8//2)
