"""
Incrementer
https://www.codewars.com/kata/590e03aef55cab099a0002e8/
"""


# return an enumerated object beginning at 1
def incrementer(nums):
    return [(i + v) % 10 for i, v in enumerate(nums, 1)]


print(incrementer([1, 2, 3]))

"""
Digitize
https://www.codewars.com/kata/5417423f9e2e6c2f040002ae/
"""


def digitize(n):
    lst = []
    for i in str(n):
        lst.append(int(i))
    return lst


print(digitize(123))

"""
Alternate case
https://www.codewars.com/kata/57a62154cf1fa5b25200031e/
"""


def alternate_case(s):
    a = ''
    for i in s:
        if i == i.lower():
            a += i.upper()

        elif i == i.upper():
            a += i.lower()
    return a


print(alternate_case("Hello World"))


# Largest pair sum in array
def largest_pair_sum(numbers):
    sorted_list = sorted(numbers, reverse=True)
    return sorted_list[0] + sorted_list[1]


(largest_pair_sum([10, 14, 2, 23, 19]))


# Character Concatenation
def char_concat(word):
    res = ''
    for i in range(len(word) // 2):
        res += word[i] + word[-1 - i] + str(i + 1)

    return res


print(char_concat("abcdef"))


# Return a sorted list of objects
def sort_list(sort_by, lst):
    return sorted(lst, key=lambda d: d[sort_by], reverse=True)


# Elevator distance
def elevator_distance(array):
    dist = 0
    for i in range(len(array) - 1):
        dist += abs(array[i] - array[i + 1])
    return dist


print(elevator_distance([5, 2, 8, 1]))


# Double Every Other

def double_every_other(lst):
    new_lst = [2 * n if i % 2 else n for i, n in enumerate(lst)]

    return new_lst


(double_every_other([1, 19, 6, 2, 12, -3]))


# List Filtering

def filter_list(l):
    res = []
    for i in l:
        if type(i) == int:
            res.append(i)
    return res


"""return a new list with the strings filtered out
The isinstance() function returns True 
if the specified object is of the specified type, otherwise False."""


def filter_list_alternative(l):
    return [i for i in l if not isinstance(i, str)]


# Square Every Digit
def square_digits(num):
    res = ''
    for n in str(num):
        res += str(int(n) ** 2)
    return int(res)


# Split In Parts
def split_in_parts(s, part_length):
    split_strings = []
    for index in range(0, len(s), part_length):
        split_strings.append(s[index: index + part_length])
    return " ".join(str(x) for x in split_strings)


print(split_in_parts('weewKKwertgdrtfyg', 4))


# Filter the number
def filter_string(string):
    letter_list = list(string)

    numbers = ''

    for letter in letter_list:
        if letter.isnumeric():
            numbers += letter

    return int(numbers)


print(filter_string('aa1bb2cc3dd'))


def filter_string_alternative(string):
    return int(filter(str.isdigit, string))


# Descending Order
def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))


print(descending_order('33335'))

# Remove HTML tags using regexp

import re

# .* mean "get everything"
# A question mark means, “The last item is optional.”

reg = re.compile('<.*?>')


def remove_html(text):
    return re.sub(reg, '', text)


(remove_html("<a href='#'>go to <b>start</b> page</a>"))


# Regexp Basics - is it all whitespace?
def whitespace(string):
    return not string or string.isspace()


print(whitespace("\t \n\r\n  "))


def whitespace_alternative(string):
    origin_len = len(string)
    string_list = string.split()
    new_string = ''.join(string_list)
    new_string_len = len(new_string)

    if string == '':
        return True
    elif origin_len != new_string_len and string.isspace():
        return True
    return False


# regex validation of 24 hours time

time = '24:00'


def validate_time(time):
    _24H = re.compile(r'^([01]?\d|2[0-3]):[0-5]\d$')
    return bool(_24H.match(time))

print(validate_time(time))

# Regex validate PIN code

"""
https://www.codewars.com/kata/55f8a9c06c018a0d6e000132

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but 
exactly 4 digits or exactly 6 digits. If the function is passed a valid PIN string, 
return true, else return false.
"""


def validate_pin(pin):
    if len(pin.strip()) < len(pin):
        return False
    elif re.match('^[0-9]*$', pin) and len(pin) == 4:
        return True
    elif re.match('^[0-9]*$', pin) and len(pin) == 6:
        return True
    else:
        return False


def validate_pin_alternative(pin):
    return len(pin) in [4, 6] and pin.isdigit()


# Regexp Basics - is it a letter?

"""
https://www.codewars.com/kata/567de72e8b3621b3c300000b

Complete the code which should return true if the given object is a single ASCII letter (lower or upper case), 
false otherwise.
"""


def is_letter(s):
    if len(s) > 1 or len(s) < 1:
        return False
    elif s == ' ':
        return False
    else:
        # search for any character that IS NOT a-z OR A-Z
        # if 'a' this will return False
        # and because of use of "not" the return value will be True as  the statement was not True
        return not re.search(r'[^a-zA-Z. ]', s)


print(is_letter(""))
print(is_letter("9"))
print(is_letter("a"))
print(is_letter("O"))


# Jaden Casing Strings

def to_jaden_case(string):
    splited_string = string.split(' ')
    new_string = ''
    for word in splited_string:
        new_string += word.capitalize() + ' '
    return new_string.strip()

print(to_jaden_case('ha ha lol'))

# Disemvowel Trolls

""""
https://www.codewars.com/kata/52fba66badcd10859f00097e

Trolls are attacking your comment section! A common way to deal with this situation is to remove all
 of the vowels from the trolls' comments, neutralizing the threat. Your task is to write a function 
 that takes a string and return a new string with all vowels removed. For example, the string 
 "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!". Note: 
 for this kata y isn't considered a vowel.
"""


def disemvowel(string_):
    vowels = ['a', 'o', 'i', 'u', 'e', 'A', 'O', 'I', 'U', 'E']
    amended_s = ''

    for char in string_:
        if char in vowels:
            amended_s += ''
        else:
            amended_s += char
    return amended_s


"""Count vowels in a string
Write a function count_vowels to count the number of vowels in a given string.
Notes: Return nil or None for non-string inputs. Return 0 if the parameter is omitted."""


def count_vowels(s=''):
    vowels = ["a", "e", "o", "u", "i"]  # create a list of vowels
    # create counter variable to keep track of values
    # while the loop is iterating values in the list
    counter = 0
    try:
        s = s.lower()
        for char in s:
            if char in vowels:
                counter += 1
        return counter
    except AttributeError:
        return None


print(count_vowels("aAbcdesdeeEfg"))


# Triple X

def triple_x(s):
    # find the first instance of "x"
    first = s.find('x')

    # get the first x and the following two characters after it:
    three_xs = s[int(first): int(first) + 3]

    if three_xs == 'xxx':
        return True
    else:
        return False


def triple_x_alternative(s):
    a = s.find("x")
    b = s.find("xxx")
    return a == b if (a > -1 and b > -1) else False


"""
Zalgo text reader
Zalgo text is text that leaks into our plane of existence from a corrupted dimension of Unicode. For example:
Complete the function that converts a string of Zalgo text into a string interpretable by our mortal eyes. For example, 
the string above would be converted into:
Have a great day!
The converted string should only feature ASCII characters.
"""
import string


def read_zalgo(zalgotext):
    printable = set(string.printable)

    return ''.join(filter(lambda x: x in printable, zalgotext))