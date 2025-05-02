#  LeetCode Problem 35: Search Insert Position
# https://leetcode.com/problems/search-insert-position/

# Solution 1: Manual Binary Search
# Time: O(log n), Space: O(1)

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while target != nums[mid] and right > left:
            if target > nums[mid]:
                left = mid + 1
                mid = (left + right) // 2
            elif target < nums[mid]:
                right =  mid
                mid = (left + right) // 2

        if target > nums[-1]:
            return mid + 1
        return mid

# Solution 2: Using built-in bisect module
# Time: O(log n), Space: O(1)

class SolutionBisect:
    def searchInsert(self, nums: List[int], target: int) -> int:
        from bisect import bisect_left
        index = bisect_left(nums, target)
        return index

my_solution = Solution()

my_list = [2, 3, 4, 5, 7]

print(my_solution.searchInsert(my_list, 5))
