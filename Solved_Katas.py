# Max diff - easy - 7Kyu
def max_diff(lst):

    if len(lst) != 0:
        return max(lst) - min(lst)
    else:
        return 0
print("The difference is", max_diff([1, 2, 3, -4]))
