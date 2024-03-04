"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters
without disturbing the relative positions of the remaining characters.
s and t consist only of lowercase English letters.
Example: "ace" is a subsequence of "abcde" while "aec" is not).

Explanations:
- define two pointers i and j to point to the initial position of the strings s and t
- each time we compare the two characters pointed to by the two pointers
- if they are the same, both pointers move right at the same time
- if they are not the same, only j moves right
- when the pointer i moves to the end of the string s, it means that s is the subsequence of t

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        # 0 0 a b
        # 0 1 a a
        # 1 2 b a
        # 1 3 b b
        
        while i < len(s) and j < len(t):  # 2 4 - four loops
            
            if s[i] == t[j]:
                i += 1
            j += 1
            
        return i == len(s)

solution = Solution()
print(solution.isSubsequence("ab", "baab"))  # true
