"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters.

s and t consist only of lowercase English letters.

Example: "ace" is a subsequence of "abcde" while "aec" is not).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        # 0 1 a b
        # 1 2 a a
        # 1 3 b a
        # 2 4 b b

        while i < len(s) and j < len(t):  # 2 4 - four loops
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)


solution = Solution()
print(solution.isSubsequence("ab", "baab"))  # true
