"""
Input: nums1 = [1,2,3], nums2 = [2,4,6]
Output: [[1,3],[4,6]]
"""


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        res = []

        set1 = set(nums1)
        set2 = set(nums2)

        return [list(set1 - set2)] + [list(set2 - set1)]


solution = Solution()
print(solution.findDifference([1, 2, 3], [2, 4, 6]))
