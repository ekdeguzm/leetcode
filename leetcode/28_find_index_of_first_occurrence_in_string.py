from typing import List


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        haystack_length = len(haystack)
        needle_length = len(needle)

        for i in range(haystack_length - needle_length + 1):
            if haystack[i:i+needle_length] == needle:
                return i
        else:
            return -1


solution = Solution()

haystack = "hello"

needle = "ll"

result = solution.strStr(haystack, needle)

print(result)
