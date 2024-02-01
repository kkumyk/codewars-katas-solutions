# - input: an odd-length array of integers, in which all of them are the same, except for one
# - output: a single different number


def stray(numbers):
    for n in numbers:
        if numbers.count(n) == 1:
            return n


print(stray([1, 1, 1, 1, 4, 1, 1, 1]))
