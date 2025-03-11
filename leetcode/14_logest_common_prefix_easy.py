from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        output = ""
        first_word = strs[0]  # Use the first word as reference

        for i in range(len(first_word)):  # Loop through characters of the first word
            for word in strs:  # Check each word
                if i >= len(word) or word[i] != first_word[i]:
                    return output  # Stop if characters don't match

            output += first_word[i]  # If all words have this char, add it

        return output


solution = Solution()

strs = ["flower", "flow", "flight"]

result = solution.longestCommonPrefix(strs)

print(f"The longest common prefix is '{result}'")
