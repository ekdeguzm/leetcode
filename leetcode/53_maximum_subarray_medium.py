from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')
        curr_sum = 0

        for i in range(len(nums)):
            # add i into currSum
            curr_sum += nums[i]

            max_sum = max(curr_sum, max_sum)

            if curr_sum < 0:
                curr_sum = 0

        return max_sum


solution = Solution()

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

result = solution.maxSubArray(nums)

print(result)
