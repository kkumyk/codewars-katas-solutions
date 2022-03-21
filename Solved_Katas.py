# Spoonerize Me

def spoonerize(words):
    a, b = words.split()
    return "{}{} {}{}".format(b[0], a[1:], a[0], b[1:])

print(spoonerize("wedding bells"))

def spoonerize(words):
    separ_words = words.split()
    update_first = separ_words[1][0:1] + separ_words[0][1:]
    update_second = separ_words[0][0:1] + separ_words[1][1:]
    return update_first + " " + update_second


# Enumerable Magic #25 - Take the First N Elements - 8Kyu

def take(arr, n):
    return arr[0:n]



inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
txt = "The store has {1} {0}, each for {2} USD."
for item in inventory:
    name = item.split(", ")[0]
    stock = item.split(", ")[1]
    price = item.split(", ")[2]
    print(txt.format(name, stock, price))

print("=========================================")

p_phrase = "was it a car or a cat I saw"


r_phrase = p_phrase[::-1]
if p_phrase == r_phrase:
    print(True)


stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"
sub = ""
for word in sent.split():
    if word not in stopwords:
        sub += word[0:2].upper() + ". "
acro = sub[:-2]

print(acro)

stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"
acro = ""
for word in org.split():
    if word not in stopwords:
        acro += word[0].upper()


scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
a_scores = 0
for n in scores.split():
    if int(n) >= 90:
        a_scores += 1

print("=========================================")

s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a', 'e', 'i', 'o', 'u']
num_vowels = 0

for char in "".join(s.split()):
    if char in vowels:
        num_vowels += 1
print(num_vowels)


sentence = "python is a high level general purpose programming language that can be applied to many different classes " \
           "of problems. "
num_a_or_e = 0
for word in sentence.split():
    if "a" in "".join(set(word)) or "e" in "".join(set(word)):
        num_a_or_e += 1
print(num_a_or_e)

items = ["whirring", "wow!", "calendar", "wry", "glass", "", "llama", "tumultuous", "owing"]
acc_num = 0
for word in items:
    if "w" in word:
        acc_num += 1
print(acc_num)

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
same_letter_count = 0
for word in sentence.split():
    if word[0] == word[-1]:
        same_letter_count += 1
print("same_letter_count", same_letter_count)

rainfall_mi = "1.65, 1.46, 2.05, 3.03, 3.35, 3.46, 2.83, 3.23, 3.5, 2.52, 2.8, 1.85"
num_rainy_months = 0
for n in rainfall_mi.split(","):
    if float(n) > 3.0:
        num_rainy_months += 1
print("num_rainy_months", num_rainy_months)

# from turtle import *
# for i in range(50):
#     forward(i)
#     left(91)

lett = ""
for n in range(7):
    lett += "b"
print(lett)

original_str = "The quick brown rhino jumped over the extremely lazy fox"
num_words_list = []

for l in original_str.split(" "):
    num_words_list.append(len(l))

print(num_words_list)

nums = []
for n in range(68):
    nums.append(n)
print(nums)

week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
num_of_items = len(week_temps_f.split(","))
avg_temp = 0
sum_temp = 0

for t in week_temps_f.split(","):
    sum_temp += float(t)
    avg_temp = sum_temp / num_of_items
print(avg_temp)

my_str = "MICHIGAN"
for l in my_str:
    print(l)

several_things = ["hello", 2, 4, 6.0, 7.5, 234352354, "the end", "", 99]
for e in several_things:
    print(e)
for i in several_things:
    print(type(i))

str_list = ["hello", "", "goodbye", "wonderful", "I love Python"]
# Write your code here.
for e in str_list:
    print(len(e))

original_str = "The quick brown rhino jumped over the extremely lazy fox."
num_chars = 0
for char in list(original_str):
    num_chars += 1
print(num_chars)

addition_str = "2+5+10+20"
sum_val = 0
for n in addition_str.split("+"):
    sum_val += int(n)
print(sum_val)


# Find the missing letter - 6Kyu

def find_missing_letter(chars):
    alphabet_lower = "".join([chr(i) for i in range(ord('a'), ord('z') + 1)])
    alphabet = alphabet_lower + alphabet_lower.upper()
    first = alphabet.index(chars[0])
    last = alphabet.index(chars[-1])
    res = alphabet[first:last + 1] + ''.join(chars)
    return ''.join([c for c in res if res.count(c) == 1])


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
print(find_missing_letter(['O', 'Q', 'R', 'S']))


# Find the unique number - 6Kyu

def find_uniq(arr):
    first = sorted(arr)[0]
    last = sorted(arr)[-1]
    if first == sorted(arr)[1]:
        return last
    else:
        return first


print(find_uniq([1, 1, 1, 2, 1, 1]))


# Count characters in your string - 6Kyu

def count(string):
    unique_chars = sorted(list(set(string)))
    counts = {}

    for k in unique_chars:
        counts[k] = string.count(k)
    return counts


print(count('aba'))


# Remove First and Last Character - 8Kyu
def remove_char(s):
    return s[1:len(s) - 1]

def remove_char(s):
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


# Difference of 2 - 6Kyu

def twos_difference(arr):
    return [(i, i + 2) for i in sorted(arr) if i + 2 in arr]


print(twos_difference([1, 2, 3, 4]))


# Sum of positive - 8Kyu

def positive_sum(arr):
    sum_nums = 0
    for n in arr:
        if n > 0:
            sum_nums += n
    return sum_nums


print(positive_sum([1, 2, 3, 4, 5]))


# Sort the odd - 6Kyu

def sort_array(source_array):
    odds_list = sorted([item for item in source_array if item % 2 != 0])
    odd_int = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odds_list[odd_int]
            odd_int += 1
    return source_array


print(sort_array([5, 3, 2, 8, 1, 4]))


# Your order, please -6Kyu

def order(sentence):
    res = ''
    for i in range(1, len(sentence)):
        for s in sentence.split():
            if str(i) in s:
                res += s + ' '
    return res.strip()


print(order("is2 Thi1s T4est 3a"))


# Remove consecutive duplicate words - 7Kyu

# List Filtering - 7Kyu
def filter_list(l):
    return [e for e in l if type(e) == int]


print(filter_list([1, 2, 'a', 'b']))


def remove_consecutive_duplicates(s):
    words = s.split(' ')
    result = words[0] + ' '
    for pos in range(1, len(words)):
        if words[pos] != words[pos - 1]:
            result += words[pos] + ' '
    return result.strip()


print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))


# Move 10 - 7Kyu

def move_ten(st):
    res = ""
    alphabet = "".join([chr(i) for i in range(ord('a'), ord('z') + 1)]) * 2
    for l in st:
        for a in alphabet:
            if l == a:
                res += alphabet[alphabet.index(a) + 10]
    return res[0::2]


print(move_ten("testcase"))


# Sum of Minimums! - 7Kyu

def sum_of_minimums(numbers):
    sum_nums = 0
    for n in numbers:
        sum_nums += min(n)
    return sum_nums


print(sum_of_minimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]]))


# What comes after?  - 7Kyu
def comes_after(words, letter):
    result = ""
    for i, c in enumerate(words):
        if c.lower() == letter.lower() and i < len(words) - 1 and words[i + 1].isalpha():
            result += words[i + 1]

    return result


def comes_after(st, l):
    res = ''
    for i, e in enumerate(st):
        if e.lower() == l.lower() and i < len(st) - 1:
            res += st[i + 1]

    return ''.join([i for i in res if i.isalpha()])


print(comes_after("Pirates say arrrrrrrrr.", 'r'))


# Reverse and Invert - 7Kyu

def reverse_invert(lst):
    """ Use list comprehension with the isinstance() function which returns True
    if the specified object is of the specified type, int in our case.
    The result is a list of integers.
    """
    nums = [num for num in lst if isinstance(num, int)]
    nums_strings = list(map(str, nums))  # Convert numbers in the list to strings.

    positive_reversed_nums = []
    plus_minus_one = []
    for e in nums_strings:
        if "-" in e:
            positive_reversed_nums.append(e.replace("-", "")[::-1])  # remove "-" and reverse
            plus_minus_one.append(1)
        else:
            positive_reversed_nums.append(e[::-1])
            plus_minus_one.append(-1)

    str_to_int = [int(x) for x in positive_reversed_nums]

    products = []
    for num1, num2 in zip(plus_minus_one, str_to_int):
        products.append(num1 * num2)
    return products


print(reverse_invert([-9, -18, 99, 'a', 9.23]))

# def test_reverse_invert():
#     assert reverse_invert([-9, -18, 99]) == [9, 81, -99]


from math import copysign as sign


def reverse_invert(lst):
    return [-int(sign(int(str(abs(x))[::-1]), x)) for x in lst if isinstance(x, int)]


# Find the middle element - 7Kyu

def gimme(input_array):
    return input_array.index(sorted(input_array)[1])


print(gimme([2, 3, 1]))


# Sum of a sequence - 7Kyu

def sequence_sum(begin_number, end_number, step):
    return sum(list(range(begin_number, end_number + 1, step)))


print(sequence_sum(2, 6, 2))


# Don't give me five! - 7Kyu

def dont_give_me_five(start, end):
    nums = list(range(start, end + 1))
    string_ints = [str(int) for int in nums]
    matching = [s for s in string_ints if "5" in s]
    return len(list(set(string_ints) - set(matching)))


print(dont_give_me_five(5, 34))


# Closest to Zero - 7Kyu
def closest(numbers):
    if 0 in numbers:
        return 0

    sorted_numbers = sorted(numbers, key=lambda x: abs(x))
    if (-sorted_numbers[0] in numbers):
        return None
    return sorted_numbers[0]


print(closest([2, 4, -1, -3]))


# Sort array by string length - 7Kyu
def sort_by_length(arr):
    el_len = []
    for e in arr:
        el_len.append(len(e))
    list_of_tuples_sorted_by_first_el = sorted(list(zip(el_len, arr)), key=lambda x: x[0])

    final_list = [sub[1] for sub in list_of_tuples_sorted_by_first_el]

    return final_list


print(sort_by_length(["beg", "life", "i", "to"]))


# Incrementer - 7Kyu
def incrementer(nums):
    res = []
    for i, n in enumerate(nums):
        res.append(int(str(n + (i + 1))[-1]))

    return res


print(incrementer([1, 2, 3]))


# Sum of integers in string - 7Kyu
# https://www.codewars.com/kata/598f76a44f613e0e0b000026/train/python
def sum_of_integers_in_string(s):
    sum = 0
    new_str = ''
    v = []
    for w in s:
        for l in w:
            v.append(l)
    print(v)
    new_strings = []
    for e in v:
        if e.isalpha():
            new_strings.append(e.replace(e, '-'))
        elif e.isdigit():
            new_strings.append(e)

    print("".join(new_strings))


# Sort Numbers - 7Kyu

def solution(nums):
    if nums:
        return sorted(nums)
    else:
        return []


print(solution([1, 2, 3, 10, 5]))


# String Merge! - 7Kyu

def string_merge(string1, string2, letter):
    res = string1[:string1.index(letter)] + string2[string2.index(letter):]
    return res


print(string_merge("hello", "world", "l"))


# Credit Card Mask - 7Kyu

# return masked string
def maskify(cc):
    if len(cc) >= 4:
        last_four_if_aval = cc[-4:]
        sub_str = (len(cc) - 4) * '#'
        return sub_str + last_four_if_aval

    elif len(cc) < 4 and len(cc) > 0:
        return cc

    else:
        return ''


print(maskify("4556364607935616"))


# Form The Minimum - 7Kyu

def min_value(digits):
    return int("".join(map(str, sorted(set(digits)))))


print(min_value([1, 3, 1]))


# Testing 1-2-3 - 7Kyu

def number(lines):
    numbered_lines = []
    for n, text in enumerate(lines):
        numbered_lines.append(str(n + 1) + ": " + text)

    return numbered_lines


print(number(["a", "b", "c"]))


# Lost number in number sequence - 7Kyu


def find_deleted_number(arr, mixed_arr):
    if len(arr) != len(mixed_arr):
        print(set(arr))
        print(set(mixed_arr))
        num_dif = list(set(arr) - set(mixed_arr))

        return int("".join(str(e) for e in num_dif))
    else:
        return 0


print(find_deleted_number([1, 2, 3, 4, 5], [3, 4, 1, 5]))


# Combine objects - 7Kyu
def combine(*args):
    comb = {}
    for i in args:
        for k, v in i.items():
            if k in comb:
                comb[k] += v
            else:
                comb[k] = v
    return comb


print(combine({'a': 10, 'b': 20, 'c': 30}, {'a': 3, 'c': 6, 'd': 3}))

"""
The items() method returns a view object. The view object contains the k-v pairs of the dictionary, as tuples in a list.
The view object will reflect any changes done to the dictionary.
"""


# Sum without highest and lowest number - 8Kyu

def sum_array(arr):
    sorted_arr = []
    sum_res = []

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


# 16+18=214 7Kyu

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


# Baby shark lyrics generator - 7Kyu
# Create a function, as short as possible, that returns baby shark lyrics.


def baby_shark_lyrics():
    d = ' doo' * 6
    prs = ['Baby ', 'Mommy ', 'Daddy ', 'Grandma ', 'Grandpa ']
    s = ""
    for p in prs:
        s += (p + 'shark,' + d + '\n') * 3 + (p + 'shark!\n')
    return s + ("Let's go hunt," + d + '\n') * 3 + ("Let's go hunt!\n") + "Run away,…"


print(baby_shark_lyrics())

# Slice the middle of a list backwards - 7Kyu
"""Write a function that takes a list of at least four elements as an argument and
returns a list of the middle two or three elements in reverse order."""


def reverse_middle(lst):
    middle = int(len(lst) / 2)
    nr_of_int_to_return = len(lst) - middle

    non_reverse_list = lst[middle - 1:nr_of_int_to_return + 1]

    reversed_list = non_reverse_list[::-1]

    return reversed_list


print("Reverse middle solution", reverse_middle([1, 2, 3, 4, 5]))

# Remove the minimum - 7Kyu
"""Given an array of integers, remove the smallest value. Do not mutate the original array/list.
If there are multiple elements with the same value, remove the one with a low"""


def remove_smallest(numbers):
    if numbers == []:
        return []
    else:
        first_occurrence_of_min = numbers.index(min(numbers))
        return numbers[:first_occurrence_of_min] + numbers[first_occurrence_of_min + 1:]


print(remove_smallest([1, 2, 3, 1, 1]))

# Sum the Repeats - 7Kyu
# sum up all numbers that appear in two or more lists in the input list


"""The standard library provides the Python defaultdict type - a dictionary-like class
behaves almost exactly like a regular Python dictionary, but if you try to access or modify a missing key,
then defaultdict will automatically create the key and generate a default value for it.
This makes defaultdict a valuable option for handling missing keys in dictionaries."""

from collections import defaultdict


def repeat_sum(l):
    count = defaultdict(int)

    for l1 in l:
        for val in set(l1):
            count[val] += 1

    return sum(k for k, v in count.items() if v > 1)


print("The sum is", repeat_sum([[1, 2], [2, 4], [3, 4, 4, 4], [123456789]]))


# Sum of a nested list - 7Kyu
def sum_nested(lst):
    total = 0
    for i in lst:
        if isinstance(i, list):  # checks if `i` is a list
            total += sum_nested(i)
        else:
            total += i
    return total


print("The sum of this nested list is:", sum_nested([1, [1], [[1]], [[[1]]]]))


# Duplicate sandwich - 7Kyu
def duplicate_sandwich(arr):
    start, end = [i for i, x in enumerate(arr) if arr.count(x) > 1]
    print(start)
    print(end)
    return arr[start + 1:end]


print(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]))


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
def unique_sum_1(lst):
    return sum(set(lst)) if lst else None


print("The unique sum of the numbers in a given list is: ", unique_sum_1([2, 3, 3, 3]))


def unique_sum_2(lst):
    return sum(list(dict.fromkeys(lst))) if lst else None


print("The unique sum of the numbers in a given list is: ", unique_sum_2([2, 3, 3, 3, 6, 666, 666]))


# Max diff - easy - 7Kyu
def max_diff(lst):
    if len(lst) != 0:
        return max(lst) - min(lst)
    else:
        return 0


print("The difference is", max_diff([1, 2, 3, -4]))
