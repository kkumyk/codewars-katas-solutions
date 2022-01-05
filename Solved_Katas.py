# Dictionary from two lists - 7Kyu

#  1. return a dict from a list of keys and a list of values
#  2. if there are not enough values, the keys for these values should be None
#  3. if there are not enough keys, these values should be ignored.

def createDict(keys, values):
    if len(keys) > len(values):
        values += (len(keys) - len(values)) * [None]
        #  zip(keys, values)  # get pairs of elements
        #  dict(zip(keys, values))  # convert to dictionary
    return dict(zip(keys, values))  # return dictionary


print(createDict(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(createDict(['a', 'b', 'c'], [1, 2, 3, 4]))


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
