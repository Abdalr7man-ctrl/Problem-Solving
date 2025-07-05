# LeetCode Problem 1945: Sum of Digits of String
# https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

class Solution:

    def getLucky(self, s: str, k: int) -> int:
        result = ""
        for j in s:
            result += str(ord(j) - 96)

        result1 = 0

        for _ in range(k):
            for num in result:
                result1 += int(num)
            result = str(result1)
            result1 = 0

        return int(result)

my_solution = Solution()

print(my_solution.getLucky("leetcode", 2))
