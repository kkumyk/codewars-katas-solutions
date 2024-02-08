class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set(["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"])
        s = list(s)  # ['h', 'e', 'l', 'l', 'o']
        right = len(s) - 1  # 4
        left = 0
                
        while left < right:

            while left < right and s[left].lower() not in vowels: # 0 < 4 and 'h' not in vowels => true => left = 1
                left += 1
            while left < right and s[right].lower() not in vowels: # 1 < 4 and 'o' not in vowels => false => right = 4
                right -= 1

            s[left], s[right] = s[right], s[left] # 'e', 'o' = 'o', 'e'
            left += 1 # left = 2
            right -= 1 # right = 3

        return "".join(s)


solution = Solution()
print(solution.reverseVowels("hello"))  # "holle"