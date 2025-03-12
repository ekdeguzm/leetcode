from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = dict()

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        ans = 0
        min_value = float('inf')

        for key, value in count.items():
            if value < min_value:
                min_value = value
                ans = key

        return ans


solution = Solution()

nums = [4, 1, 2, 1, 2]

result = solution.singleNumber(nums)

print(f"The single number is {result}.")
