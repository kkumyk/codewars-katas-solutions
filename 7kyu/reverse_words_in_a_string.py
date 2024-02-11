class Solution:
    def reverseWords(self, s: str) -> str:
        res = []

        while "  " in s:
            s = s.replace("  ", " ")

        trimmed = s.strip().split(" ")[::-1]  # remove spaces, split and reverse

        for w in trimmed:
            res.append(w)

        return " ".join(res)


solution = Solution()
print(solution.reverseWords("  the    sky is blue   "))  # blur is sky the
