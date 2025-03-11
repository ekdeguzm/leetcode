class Solution:
    def romanToInt(self, s: str) -> int:
        number = 0  # Initialize number
        for i in range(len(s)):
            if s[i] == "M":
                number += 1000
            elif s[i] == "D":
                number += 500
            elif s[i] == "C":
                # Check if C is before D or M (like in "CM" or "CD")
                if i < len(s) - 1 and (s[i + 1] == "D" or s[i + 1] == "M"):
                    number -= 100
                else:
                    number += 100
            elif s[i] == "L":
                number += 50
            elif s[i] == "X":
                # Check if X is before L or C (like in "XL" or "XC")
                if i < len(s) - 1 and (s[i + 1] == "L" or s[i + 1] == "C"):
                    number -= 10
                else:
                    number += 10
            elif s[i] == "V":
                number += 5
            elif s[i] == "I":
                # Check if I is before V or X (like in "IV" or "IX")
                if i < len(s) - 1 and (s[i + 1] == "V" or s[i + 1] == "X"):
                    number -= 1
                else:
                    number += 1

        return number


# Create an instance of Solution
solution = Solution()

# Test with "MCMXCIV"
s = "MCMXCIV"
result = solution.romanToInt(s)

# Print the result
print(f"Roman numeral {s} converts to integer: {result}")
