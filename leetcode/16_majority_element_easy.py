from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # create dictionary
        count = dict()

        # interate through nums and get the number
        for num in nums:
            if num in count:                # if number is in dictionary
                count[num] += 1             # add 1 to the value of it
            else:
                count[num] = 1              # begin it

            max_count = -1                  # initialize max_count
            ans = -1                        # initialize ans

            for key, val in count.items():   # iterate through dictionary
                if val > max_count:
                    max_count = val         # set the new highest max_count
                    ans = key               # key is the ans

        return ans                          # return that value


solution = Solution()

nums = [2, 2, 1, 1, 1, 2, 2]

result = solution.majorityElement(nums)

print(result)
