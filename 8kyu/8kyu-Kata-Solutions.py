# Enumerable Magic #25 - Take the First N Elements - 8Kyu
def take(arr, n):
    return arr[0:n]

# Remove First and Last Character - 8Kyu
def remove_char(s):
    return s[1:len(s) - 1]

def remove_char_alternative(s):
    return s[1:-1]

# String to number - 8Kyu
def string_to_number(s):
    return int(s)

# Double Char - 8Kyu
def double_char(s):
    new_string = ""
    for char in s:
        new_string += char*2
    return new_string
print(double_char("String"))

# String repeat - 8Kyu
def repeat_str(repeat, string):
    return string * repeat
print(repeat_str(4, 'a'))

# Sum of positive - 8Kyu
def positive_sum(arr):
    sum_nums = 0
    for n in arr:
        if n > 0:
            sum_nums += n
    return sum_nums
print(positive_sum([1, 2, 3, 4, 5]))

def remove_consecutive_duplicates(s):
    words = s.split(' ')
    result = words[0] + ' '
    for pos in range(1, len(words)):
        if words[pos] != words[pos - 1]:
            result += words[pos] + ' '
    return result.strip()
print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))

def comes_after(st, l):
    res = ''
    for i, e in enumerate(st):
        if e.lower() == l.lower() and i < len(st) - 1:
            res += st[i + 1]
    return ''.join([i for i in res if i.isalpha()])
print(comes_after("Pirates say arrrrrrrrr.", 'r'))

from math import copysign as sign
def reverse_invert(lst):
    return [-int(sign(int(str(abs(x))[::-1]), x)) for x in lst if isinstance(x, int)]

# Sum without highest and lowest number - 8Kyu
def sum_array(arr):
    if not arr:
        return 0

    elif arr:
        sorted_arr = sorted(arr)

        if len(sorted_arr) > 1:
            sum_res = sorted_arr[1:-1]
            return sum(sum_res)
        elif len(sorted_arr) == 1:
            return 0
    else:
        return 0
print(sum_array([6, 2, 1, 8, 10]))

# Difference of Volumes of Cuboids - 8kYU
def find_difference(a, b):
    x = a[0] * a[1] * a[2]
    y = b[0] * b[1] * b[2]
    return max(x, y) - min(x, y)
print(find_difference([2, 2, 3], [5, 4, 1]))

def add(num1, num2):
    odd_one = []
    sum_nums = []
    one = [int(i) for i in str(num1)]
    two = [int(i) for i in str(num2)]

    if len(one) < len(two):
        len_dif = int(len(two) - len(one))
        d = two[:len_dif]
        temp_list = two[len_dif:]
        sum_nums += [sum(pair) for pair in zip(temp_list, one)]
        string_ints = [str(int) for int in d] + [str(int) for int in odd_one] + [str(int) for int in sum_nums]
        str_of_ints = int("".join(string_ints))
        return str_of_ints

    elif len(one) > len(two):
        len_dif = int(len(one) - len(two))
        d = one[:len_dif]
        temp_list = one[len_dif:]
        sum_nums += [sum(pair) for pair in zip(temp_list, two)]
        string_ints = [str(int) for int in d] + [str(int) for int in odd_one] + [str(int) for int in sum_nums]
        str_of_ints = int("".join(string_ints))
        return str_of_ints
    else:
        sum_nums += [sum(pair) for pair in zip(one, two)]
        string_ints = [str(int) for int in sum_nums]
        str_of_ints = int("".join(string_ints))
        return str_of_ints
print(add(122, 81))

# Is it a palindrome? - 8Kyu
def is_palindrome(s):
    return s.lower() == s.lower()[::-1]
print(is_palindrome('AAAAAAAAAAAAAAAAAAAAAAA'))

# Is it even? - 8Kyu
def is_even(n):
    return (n % 2) == 0

# Area or Perimeter - 8Kyu
"""You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter."""
def area_or_perimeter(l, w):
    if l == w:
        return l * w
    else:
        return l * 2 + w * 2
print(area_or_perimeter(3, 3))

# String cleaning - 8Kyu
def string_clean(s):
    return ''.join([i for i in s if not i.isdigit()])
print(string_clean('E3at m2e2!'))

# repeatIt - 8Kyu
# Create a function that takes a string and an integer (n).
# The function should return a string that repeats the input string n number of times.
# If anything other than a string is passed in you should return "Not a string"
def repeat_it(string, n):
    return string * n if type(string) == str else 'Not a string'
print(repeat_it("*-*", 5))

# Alternative solution using isinstance function which returns True if the specified object is of the specified type,
# otherwise False:
def repeat_it(string, n):
    return string * n if isinstance(string, str) else 'Not a string'
print(repeat_it("*^*", 5))

from collections import defaultdict
def repeat_sum(l):
    count = defaultdict(int)
    for l1 in l:
        for val in set(l1):
            count[val] += 1

    return sum(k for k, v in count.items() if v > 1)

#  Capitalization and Mutability - 8Kyu
# fix the function below:
# def capitalize_word(word):
#     return "".join(char.upper() for char in word)

def capitalize_word(word):
    return word.capitalize()
print(capitalize_word('word'))


def unique_sum_2(lst):
    return sum(list(dict.fromkeys(lst))) if lst else None
print("The unique sum of the numbers in a given list is: ", unique_sum_2([2, 3, 3, 3, 6, 666, 666]))