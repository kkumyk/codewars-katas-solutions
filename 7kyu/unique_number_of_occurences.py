"""
Given an array of integers arr, return true if the number of occurrences is unique or false otherwise.
Input: arr = [1,2,2,1,1,3]
Output: true
Explanation:
The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
"""


class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:

        counts = []
        uniques = list(set(arr))

        for u in uniques:
            counts.append(arr.count(u))

        return sorted(counts) == sorted(set(counts))


solution = Solution()
print(solution.uniqueOccurrences([1, 2, 2, 1, 1, 3]))  # true
