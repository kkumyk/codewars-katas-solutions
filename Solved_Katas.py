# Isograms - 7Kyu
def is_isogram(string):
    unique_len = len(set(string.lower()))
    if unique_len < len(string):
        return False
    else:
        return True

print("Is this string an isogram? ", is_isogram('aba'))
print("Is this string an isogram? ", is_isogram('Dermatoglyphics'))


# Unique Sum - 7Kyu
def unique_sum(lst):
    return sum(set(lst)) if lst else None
print("The unique sum of the numbers in a given list is: ", unique_sum([2, 3, 3, 3]))

# Max diff - easy - 7Kyu
def max_diff(lst):

    if len(lst) != 0:
        return max(lst) - min(lst)
    else:
        return 0
print("The difference is", max_diff([1, 2, 3, -4]))
