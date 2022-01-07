# Duplicate sandwich - 7Kyu
def duplicate_sandwich(arr):
    start, end = [i for i, x in enumerate(arr) if arr.count(x) > 1]
    print(start)
    print(end)
    return arr[start+1:end]


print(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]))

# String cleaning - 8Kyu
def string_clean(s):
    return ''.join([i for i in s if not i.isdigit()])


print(string_clean('E3at m2e2!'))


# repeatIt - 8Kyu

# Create a function that takes a string and an integer (n).
# The function should return a string that repeats the input string n number of times.
# If anything other than a string is passed in you should return "Not a string"
def repeat_it(string,n):
    return string * n if type(string) == str else 'Not a string'

print(repeat_it("*-*", 5))


# Alternative solution using isinstance function which returns True if the specified object is of the specified type,
# otherwise False:

def repeat_it(string, n):
    return string * n if isinstance(string, str) else 'Not a string'

print(repeat_it("*^*", 5))

#  Capitalization and Mutability - 8Kyu
# fix the function below:
# def capitalize_word(word):
#     return "".join(char.upper() for char in word)

def capitalize_word(word):
    return word.capitalize()

capitalize_word('word')


#  Disorganised page lists - 7Kyu

#  return an array with numbers that are out of place

def find_page_number(pages):
    n, miss = 1, []  # set n to 1 and an empty array miss for misplaced numbers

    for i in pages:
        if i != n:
            miss.append(i)
        else:
            n += 1
    return miss


print(find_page_number([1, 2, 10, 3, 4, 5, 8, 6, 7]))


#  Map over a list of lists - 7Kyu
#  Write a function which maps a function over the lists in a list

def grid_map(lst, op):  # which performs op(element) for all elements of lst
    return [[*map(op, x)] for x in lst]


# A List Comprehension follows the basic pattern:
# [ <do something to item>  for  <item> in <list>]

char_grid = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]
print(grid_map(char_grid, lambda x: x.upper()))


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
