from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left_pointer = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[left_pointer] = nums[r]
                left_pointer += 1
        return left_pointer


solution = Solution()

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

result = solution.removeDuplicates(nums)

print(result)
