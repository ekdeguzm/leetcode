from typing import List


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        count = 0
        i = length - 1  # Start from the last character

        # Step 1: Ignore trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # Step 2: Count the characters of the last word
        while i >= 0 and s[i] != " ":
            count += 1
            i -= 1

        return count


solution = Solution()

s = "  fly me   to  the moon  "

result = solution.lengthOfLastWord(s)

print(result)
