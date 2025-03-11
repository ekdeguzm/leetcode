from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        count = {}

        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1

            max_count = -1
            ans = -1

            for key, val in count.items():
                if val > max_count:
                    max_count = val
                    ans = key

        return ans


solution = Solution()

nums = [2, 2, 1, 1, 1, 2, 2]

result = solution.majorityElement(nums)

print(result)
