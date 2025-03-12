from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:

        list = [1, 2, 3]
        if n == 1:
            return 1

        if n == 2:
            return 2

        if n == 3:
            return 3

        for i in range(1, n-2):
            num = list[i] + list[i+1]
            list.append(num)

        return list[-1]


solution = Solution()

n = 5

result = solution.climbStairs(n)

print(f"The number of ways to climb stairs with {n} steps is {result}")
