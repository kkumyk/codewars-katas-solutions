"""
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
"""


class Solution:
    def moveZeroes(self, nums: list[int]):
        pos = 0

        for i in range(len(nums)):  # i = 0 1 2 3 4
            if not nums[i]:  # returns True when the found number is not zero: 1 3 12
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
        return nums


solution = Solution()
print(solution.moveZeroes([0, 1, 0, 3, 12]))  # [1,3,12,0,0]
