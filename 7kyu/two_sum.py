"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)  # 6

        for i in range(n - 1):  # 0 in range 5

            for j in range(i + 1, n):  # 0 in range(1, 6)

                if nums[i] + nums[j] == target: # 2 + 7
                    return [i, j]
        return []  # No solution found


solution = Solution()
print(solution.twoSum([2, 7, 4, 3, 11, 15], 9))  # [0, 1]


# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:

#         prevMap = {}  # val : index

#         for i, n in enumerate(nums):
#             diff = target - n  # 7 2 5 6 -2 -6

#             if diff in prevMap:
#                 return [prevMap[diff], i]
#             prevMap[n] = i

#         return
