# class Solution:
#     def removeMarkedElements(self, arr1: list, arr2: list) -> list:

#         result = []

#         for i in arr1:
#             if i not in arr2:
#                 result.append(i)
#         return result


class Solution:
    def removeMarkedElements(self, integer_list: list, values_list: list) -> list:
        return [i for i in integer_list if i not in values_list]


solution = Solution()
print(solution.removeMarkedElements([1, 1, 2, 3, 1, 2, 3, 4], [1, 3]))  # [2,2,4]
