"""
Input: nums = [2,7,11,15], target = 9
Output: [0,1]

- there is exactly one solution >> we don't need to worry about not finding a solution

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         n = len(nums)  # 6

#         for i in range(n - 1):  # 0 in range 5
#             for j in range(i + 1, n):  # 0 in range(1, 6)
#                 if nums[i] + nums[j] == target:  # 2 + 7
#                     return [i, j]
#         return []  # No solution found

"""
Hashmap Solution
- we are going to map the value to the index
- we going to iterate over the array only once

"""

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap = {}  # mapping val:index

        for i, n in enumerate(nums):
            diff = target - n  # with n being nums[i] will result in: 7 2 5 6 -2 -6

            if diff in prevMap: # check if the difference is already in the hashmap
                return [prevMap[diff], i] # if so then return the solution of the pair of the indices
            prevMap[n] = i # if we don't find the solution then we need to update the hashmap
        return # since we know that a solution exists, we don't need to return anything

solution = Solution()
print(solution.twoSum([2, 7, 4, 3, 11, 15], 9))  # [0, 1]
