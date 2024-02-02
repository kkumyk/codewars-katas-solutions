# Write a function that doubles every second integer in a list, starting from the left.


def double_every_other(a):
    result = []

    for idx, n in enumerate(a):
        if idx % 2 != 0:
            result.append(n * 2)
        else:
            result.append(n)

    return result


print(double_every_other([1, 2, 3, 4]))  # [1,4,3,8]
