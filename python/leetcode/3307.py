# 3307. Find the K-th Character in String Game II
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-ii/description/
from typing import List

class Solution:
    def shift(self, word: str) -> str:
        new_word = ""
        for i in word:
            new_word += chr(ord(i) + 1)
        return new_word

    def kthCharacter(self, k: int, operations: List[int]) -> str:
        word = "a"
        for i in operations:
            if i == 0:
                word += word
            elif i == 1:
                word += self.shift(word)
        return word[k - 1]

mySolution = Solution()

print(mySolution.kthCharacter(10, [0, 1, 0, 1]))
