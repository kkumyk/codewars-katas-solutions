# Given an input of an array of digits, return the array with each digit incremented by its position in the array:
# the first digit will be incremented by 1, the second digit by 2, etc.
# Make sure to start counting your positions from 1 ( and not 0 ).


def incrementer(num):
    result = []

    for idx, n in enumerate(num, 1):
        result.append((n + idx) % 10)

    return result


print(incrementer([4, 6, 7, 1, 3]))  # [5, 8, 0, 5, 8]
