from typing import List


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:

        if n <= 0:
            return False

        for i in range(100):
            if 2**i == n:
                return True
        return False


solution = Solution()

n = 16

result = solution.isPowerOfTwo(n)

print(result)
