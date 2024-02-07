# Input: candies = [2,3,5,1,3], extraCandies = 3
# Output: [true,true,true,false,true]
# Explanation: The current max value is 5 which is held by Kid 3

# Kid 1, they will have 2 + 3 = 5 candies, which is greater or equal to the current max of 5.
# Kid 2, they will have 3 + 3 = 6 candies, which is greater or equal to the current max of 5.
# Kid 3, they will have 5 + 3 = 8 candies, which is greater or equal to the current max of 5.
# Kid 4, they will have 1 + 3 = 4 candies, which is less than the current max of 5.
# Kid 5, they will have 3 + 3 = 6 candies, which is greater or equal to the current max of 5.


def kidsWithCandies(candies, extraCandies):

    result = []

    currMax = max(candies)
    for c in candies:
        result.append(c + extraCandies >= currMax)

    return result


print(kidsWithCandies([2, 3, 5, 1, 3], 3))
