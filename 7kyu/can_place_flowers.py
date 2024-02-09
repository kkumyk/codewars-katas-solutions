"""
INPUT:
a flowerbed: flowers cannot be planted in adjacent plots
0 = empty and 1 = not empty
n - new flowers

OUTPUT:
true if n can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

For the solution we need two variables: 
    count - number of flowers we can plant
    prev - what was on the previous plot

We iterate over plots and see what are the previous and current plots in four cases to check.
Depending on that we increase or decrease the count

prev | cur
1    |  0  => cannot plant => prev = 0
0    |  1  => cannot plant => prev = 1
0    |  0  => can plant    => count++; prev = 1
1    |  1  => violation    => count--; prev = 1
"""

class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count, prev = 0, 0
        
        for cur in flowerbed:
            if cur == 1:
                if prev == 1: # violation
                    count -= 1
                prev = 1
            else:
                if prev == 1: # cannot plant
                    prev = 0
                else:
                    count += 1
                    prev = 1  # can plant
        return count >= n


solution = Solution()
print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # True
