"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters.

s and t consist only of lowercase English letters.

Example: "ace" is a subsequence of "abcde" while "aec" is not).
"""


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        one, two  = "", ""
        del_chars = list(set(t) - set(s))
        
        for l in list(s):
            if l not in del_chars:
                one += l
        
        for x in list(t):
            if x not in del_chars:
                two += x
        
        return one == two

solution = Solution()
print(solution.isSubsequence("abc", "ahbgdc"))  # true
