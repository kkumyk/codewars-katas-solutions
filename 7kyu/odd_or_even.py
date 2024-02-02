# Solution 1
def odd_or_even(arr):
    if sum(arr) % 2 != 0:
        return "odd"
    return "even"


# Solution 2
def odd_or_even(arr):
    return "odd" if sum(arr) % 2 != 0 else "even"


print(odd_or_even([0, 1, 2]))  # "odd"
