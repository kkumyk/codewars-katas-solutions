"""
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * (len(nums))  # produces [1, 1, 1, 1]
        prefix = 1  # 1 as there is no prefix for the first element in the array
        for i in range(len(nums)): # 0 1 2 3
            res[i] = prefix        # 1
            prefix *= nums[i]
        # res looks as [1, 1, 2, 6] as the elements in the initial array of [1, 1, 1, 1] were multiplied by prev elements of the array
        # the first element is a default value of 1 as the very first el does not have a prefix
        # the 3*4 from the nums won't be stored as there is no more space in the result array
        # so the three el prior to 4 will be multiplied with the prev el and stored in the res array
        # the multiplication will be done from the beginning of the array up to the last el(4): 1*1, 1*2, 2*3

        postfix = 1
        for i in range(len(nums) - 1, -1, -1): # start at the end of the input array and go up until the beginning of the array: 3 2 1 0
            res[i] *= postfix  # multiply by value that is already in the results [1, 1, 2, 6] with the postfix which is 1 here
            postfix *= nums[i] # here we can continuously update the postfix by the values found in the input array nums
        return res
    
solution = Solution()
print(solution.productExceptSelf([1, 2, 3, 4]))  # [24,12,8,6]

# Followed solution explanations at https://www.youtube.com/watch?v=bNvIQI2wAjk&t=1s