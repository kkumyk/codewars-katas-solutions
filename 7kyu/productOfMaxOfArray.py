from math import prod

def maxProduct(numbers, size):
    return prod(sorted(numbers)[-size:])

print(maxProduct([10, 8, 7, 9], 3))  # 720
