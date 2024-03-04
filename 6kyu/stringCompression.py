# https://leetcode.com/problems/string-compression/solutions/3245804/clean-codes-full-explanation-two-pointers-c-java-python3/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def compress(self, chars: list[str]) -> int:
        comp_i = 0  # keep track of the current position in the compressed array
        i = 0  # iterate over the original character array
        # iterate over the whole group of characters, set the counter to zero
        while i < len(chars):
            letter = chars[i] # set the current letter to the first character int he array
            count = 0
            # iterate over the sub-group of consecutive characters and count them
            while i < len(chars) and chars[i] == letter:
                count += 1
                i += 1
            # covers the case when the a different character is found or the end of the array is reached
            # change the array inplace by setting the first char of comp array
            chars[comp_i] = letter # write the current letter to the compressed array: a, b, c
            comp_i += 1 # tracks the position for inserting of the count in the compressed array: 1, 3, 5
            if count > 1:
              for c in str(count): # write the count as a string to the compressed array
                chars[comp_i] = c # write the current count to the compressed array: 2, 2, 3
                comp_i += 1
        return comp_i

solution = Solution()
print(solution.compress(["a", "a", "b", "b", "c", "c", "c"]))  # ["a","2","b","2","c","3"]


# # https://leetcode.com/problems/string-compression/?envType=study-plan-v2&envId=leetcode-75
# class Solution:
#     def compress(self, chars: list[str]) -> int:
#         i = 0
#         count = 1
#         while (i < len(chars) - 1):  # as long as the index < number of elements in the list
#             if chars[i+1]==chars[i]: # if element next == element current
#                 chars.pop(i+1)       # remove element next
#                 count+=1             # add 1 to count

#             # the case where the following char is not the same as the previous one
#             elif count>1: # if the count is greater than 1 due to prev checks, it means that we have a group of repeating chars to compress
#                 cc=[*str(count)] # convert the count into a list of individual digits: ["2"]

#                 # it then iterates over this ["2"] list, inserts each digit into the chars array, and increments i accordingly
#                 # this step ensures that groups with lengths of 10 or more are properly split into multiple characters
#                 for j in range(len(cc)): # 1
#                     print(j)
#                     chars.insert(i+j+1,cc[j])
#                 count=1
#                 i+=len(cc)+1

#             # if the count is not greater than 1, we have a single char occurrence,
#             # so the algorithm moves to the next character by incrementing i
#             else:
#                 i+=1

#         # after the while loop, the algorithm checks if there is a remaining group of repeating characters that have not been compressed.
#         # if count is greater than 1, the algorithm converts it into a list of digits and appends each digit to the chars array.
#         if count>1:
#             chars+=[*str(count)]

#         # finally, the algorithm returns the length of the modified chars array
#         return  len(chars)
