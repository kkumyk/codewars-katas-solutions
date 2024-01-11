// """
// Alternate case
// https://www.codewars.com/kata/57a62154cf1fa5b25200031e/
// """
// def alternate_case(s):
//     a = ''
//     for i in s:
//         if i == i.lower():
//             a += i.upper()

//         elif i == i.upper():
//             a += i.lower()
//     return a
// print(alternate_case("Hello World"))


// # Largest pair sum in array
// def largest_pair_sum(numbers):
//     sorted_list = sorted(numbers, reverse=True)
//     return sorted_list[0] + sorted_list[1]


// (largest_pair_sum([10, 14, 2, 23, 19]))


// # Character Concatenation
// def char_concat(word):
//     res = ''
//     for i in range(len(word) // 2):
//         res += word[i] + word[-1 - i] + str(i + 1)

//     return res


// print(char_concat("abcdef"))


// # Return a sorted list of objects
// def sort_list(sort_by, lst):
//     return sorted(lst, key=lambda d: d[sort_by], reverse=True)


// # Elevator distance
// def elevator_distance(array):
//     dist = 0
//     for i in range(len(array) - 1):
//         dist += abs(array[i] - array[i + 1])
//     return dist


// print(elevator_distance([5, 2, 8, 1]))


// # Double Every Other

// def double_every_other(lst):
//     new_lst = [2 * n if i % 2 else n for i, n in enumerate(lst)]

//     return new_lst


// (double_every_other([1, 19, 6, 2, 12, -3]))


// # List Filtering

// def filter_list(l):
//     res = []
//     for i in l:
//         if type(i) == int:
//             res.append(i)
//     return res


// """return a new list with the strings filtered out
// The isinstance() function returns True 
// if the specified object is of the specified type, otherwise False."""


// def filter_list_alternative(l):
//     return [i for i in l if not isinstance(i, str)]


// # Square Every Digit
// def square_digits(num):
//     res = ''
//     for n in str(num):
//         res += str(int(n) ** 2)
//     return int(res)


// # Split In Parts
// def split_in_parts(s, part_length):
//     split_strings = []
//     for index in range(0, len(s), part_length):
//         split_strings.append(s[index: index + part_length])
//     return " ".join(str(x) for x in split_strings)


// print(split_in_parts('weewKKwertgdrtfyg', 4))


// # Filter the number
// def filter_string(string):
//     letter_list = list(string)

//     numbers = ''

//     for letter in letter_list:
//         if letter.isnumeric():
//             numbers += letter

//     return int(numbers)


// print(filter_string('aa1bb2cc3dd'))


// def filter_string_alternative(string):
//     return int(filter(str.isdigit, string))


// # Descending Order
// def descending_order(num):
//     return int("".join(sorted(str(num), reverse=True)))


// print(descending_order('33335'))

// # Remove HTML tags using regexp

// import re

// # .* mean "get everything"
// # A question mark means, “The last item is optional.”

// reg = re.compile('<.*?>')


// def remove_html(text):
//     return re.sub(reg, '', text)


// (remove_html("<a href='#'>go to <b>start</b> page</a>"))


// # Regexp Basics - is it all whitespace?
// def whitespace(string):
//     return not string or string.isspace()


// print(whitespace("\t \n\r\n  "))


// def whitespace_alternative(string):
//     origin_len = len(string)
//     string_list = string.split()
//     new_string = ''.join(string_list)
//     new_string_len = len(new_string)

//     if string == '':
//         return True
//     elif origin_len != new_string_len and string.isspace():
//         return True
//     return False


// # regex validation of 24 hours time

// time = '24:00'


// def validate_time(time):
//     _24H = re.compile(r'^([01]?\d|2[0-3]):[0-5]\d$')
//     return bool(_24H.match(time))

// print(validate_time(time))

// # Regex validate PIN code

// """
// https://www.codewars.com/kata/55f8a9c06c018a0d6e000132

// ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but 
// exactly 4 digits or exactly 6 digits. If the function is passed a valid PIN string, 
// return true, else return false.
// """


// def validate_pin(pin):
//     if len(pin.strip()) < len(pin):
//         return False
//     elif re.match('^[0-9]*$', pin) and len(pin) == 4:
//         return True
//     elif re.match('^[0-9]*$', pin) and len(pin) == 6:
//         return True
//     else:
//         return False


// def validate_pin_alternative(pin):
//     return len(pin) in [4, 6] and pin.isdigit()


// # Regexp Basics - is it a letter?

// """
// https://www.codewars.com/kata/567de72e8b3621b3c300000b

// Complete the code which should return true if the given object is a single ASCII letter (lower or upper case), 
// false otherwise.
// """


// def is_letter(s):
//     if len(s) > 1 or len(s) < 1:
//         return False
//     elif s == ' ':
//         return False
//     else:
//         # search for any character that IS NOT a-z OR A-Z
//         # if 'a' this will return False
//         # and because of use of "not" the return value will be True as  the statement was not True
//         return not re.search(r'[^a-zA-Z. ]', s)


// print(is_letter(""))
// print(is_letter("9"))
// print(is_letter("a"))
// print(is_letter("O"))


// # Jaden Casing Strings

// def to_jaden_case(string):
//     splited_string = string.split(' ')
//     new_string = ''
//     for word in splited_string:
//         new_string += word.capitalize() + ' '
//     return new_string.strip()

// print(to_jaden_case('ha ha lol'))

// # Disemvowel Trolls

// """"
// https://www.codewars.com/kata/52fba66badcd10859f00097e

// Trolls are attacking your comment section! A common way to deal with this situation is to remove all
//  of the vowels from the trolls' comments, neutralizing the threat. Your task is to write a function 
//  that takes a string and return a new string with all vowels removed. For example, the string 
//  "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!". Note: 
//  for this kata y isn't considered a vowel.
// """


// def disemvowel(string_):
//     vowels = ['a', 'o', 'i', 'u', 'e', 'A', 'O', 'I', 'U', 'E']
//     amended_s = ''

//     for char in string_:
//         if char in vowels:
//             amended_s += ''
//         else:
//             amended_s += char
//     return amended_s


// """Count vowels in a string
// Write a function count_vowels to count the number of vowels in a given string.
// Notes: Return nil or None for non-string inputs. Return 0 if the parameter is omitted."""


// def count_vowels(s=''):
//     vowels = ["a", "e", "o", "u", "i"]  # create a list of vowels
//     # create counter variable to keep track of values
//     # while the loop is iterating values in the list
//     counter = 0
//     try:
//         s = s.lower()
//         for char in s:
//             if char in vowels:
//                 counter += 1
//         return counter
//     except AttributeError:
//         return None


// print(count_vowels("aAbcdesdeeEfg"))


// # Triple X

// def triple_x(s):
//     # find the first instance of "x"
//     first = s.find('x')

//     # get the first x and the following two characters after it:
//     three_xs = s[int(first): int(first) + 3]

//     if three_xs == 'xxx':
//         return True
//     else:
//         return False


// def triple_x_alternative(s):
//     a = s.find("x")
//     b = s.find("xxx")
//     return a == b if (a > -1 and b > -1) else False


// """
// Zalgo text reader
// Zalgo text is text that leaks into our plane of existence from a corrupted dimension of Unicode. For example:
// Complete the function that converts a string of Zalgo text into a string interpretable by our mortal eyes. For example, 
// the string above would be converted into:
// Have a great day!
// The converted string should only feature ASCII characters.
// """
// import string


// def read_zalgo(zalgotext):
//     printable = set(string.printable)

//     return ''.join(filter(lambda x: x in printable, zalgotext))

// # Spoonerize Me - 7Kyu

// def spoonerize(words):
//     a, b = words.split()
//     return "{}{} {}{}".format(b[0], a[1:], a[0], b[1:])

// print(spoonerize("wedding bells"))

// def spoonerize(words):
//     separ_words = words.split()
//     update_first = separ_words[1][0:1] + separ_words[0][1:]
//     update_second = separ_words[0][0:1] + separ_words[1][1:]
//     return update_first + " " + update_second

// # Remove consecutive duplicate words - 7Kyu
// def remove_consecutive_duplicates(s):
//     words = s.split(' ')
//     result = words[0] + ' '
//     for pos in range(1, len(words)):
//         if words[pos] != words[pos - 1]:
//             result += words[pos] + ' '
//     return result.strip()

// print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))


// # Move 10 - 7Kyu

// def move_ten(st):
//     res = ""
//     alphabet = "".join([chr(i) for i in range(ord('a'), ord('z') + 1)]) * 2
//     for l in st:
//         for a in alphabet:
//             if l == a:
//                 res += alphabet[alphabet.index(a) + 10]
//     return res[0::2]


// print(move_ten("testcase"))


// # Sum of Minimums! - 7Kyu

// def sum_of_minimums(numbers):
//     sum_nums = 0
//     for n in numbers:
//         sum_nums += min(n)
//     return sum_nums


// print(sum_of_minimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]]))


// # What comes after?  - 7Kyu
// def comes_after(words, letter):
//     result = ""
//     for i, c in enumerate(words):
//         if c.lower() == letter.lower() and i < len(words) - 1 and words[i + 1].isalpha():
//             result += words[i + 1]

//     return result


// def comes_after(st, l):
//     res = ''
//     for i, e in enumerate(st):
//         if e.lower() == l.lower() and i < len(st) - 1:
//             res += st[i + 1]

//     return ''.join([i for i in res if i.isalpha()])


// print(comes_after("Pirates say arrrrrrrrr.", 'r'))


// # Reverse and Invert - 7Kyu

// def reverse_invert(lst):
//     """ Use list comprehension with the isinstance() function which returns True
//     if the specified object is of the specified type, int in our case.
//     The result is a list of integers.
//     """
//     nums = [num for num in lst if isinstance(num, int)]
//     nums_strings = list(map(str, nums))  # Convert numbers in the list to strings.

//     positive_reversed_nums = []
//     plus_minus_one = []
//     for e in nums_strings:
//         if "-" in e:
//             positive_reversed_nums.append(e.replace("-", "")[::-1])  # remove "-" and reverse
//             plus_minus_one.append(1)
//         else:
//             positive_reversed_nums.append(e[::-1])
//             plus_minus_one.append(-1)

//     str_to_int = [int(x) for x in positive_reversed_nums]

//     products = []
//     for num1, num2 in zip(plus_minus_one, str_to_int):
//         products.append(num1 * num2)
//     return products


// print(reverse_invert([-9, -18, 99, 'a', 9.23]))


// from math import copysign as sign


// def reverse_invert(lst):
//     return [-int(sign(int(str(abs(x))[::-1]), x)) for x in lst if isinstance(x, int)]


// # Find the middle element - 7Kyu

// def gimme(input_array):
//     return input_array.index(sorted(input_array)[1])


// print(gimme([2, 3, 1]))


// # Sum of a sequence - 7Kyu

// def sequence_sum(begin_number, end_number, step):
//     return sum(list(range(begin_number, end_number + 1, step)))


// print(sequence_sum(2, 6, 2))


// # Don't give me five! - 7Kyu

// def dont_give_me_five(start, end):
//     nums = list(range(start, end + 1))
//     string_ints = [str(int) for int in nums]
//     matching = [s for s in string_ints if "5" in s]
//     return len(list(set(string_ints) - set(matching)))


// print(dont_give_me_five(5, 34))


// # Closest to Zero - 7Kyu
// def closest(numbers):
//     if 0 in numbers:
//         return 0

//     sorted_numbers = sorted(numbers, key=lambda x: abs(x))
//     if (-sorted_numbers[0] in numbers):
//         return None
//     return sorted_numbers[0]


// print(closest([2, 4, -1, -3]))


// # Sort array by string length - 7Kyu
// def sort_by_length(arr):
//     el_len = []
//     for e in arr:
//         el_len.append(len(e))
//     list_of_tuples_sorted_by_first_el = sorted(list(zip(el_len, arr)), key=lambda x: x[0])

//     final_list = [sub[1] for sub in list_of_tuples_sorted_by_first_el]

//     return final_list


// print(sort_by_length(["beg", "life", "i", "to"]))


// # Incrementer - 7Kyu
// def incrementer(nums):
//     res = []
//     for i, n in enumerate(nums):
//         res.append(int(str(n + (i + 1))[-1]))

//     return res


// print(incrementer([1, 2, 3]))


// # Sum of integers in string - 7Kyu
// # https://www.codewars.com/kata/598f76a44f613e0e0b000026/train/python
// def sum_of_integers_in_string(s):
//     sum = 0
//     new_str = ''
//     v = []
//     for w in s:
//         for l in w:
//             v.append(l)
//     print(v)
//     new_strings = []
//     for e in v:
//         if e.isalpha():
//             new_strings.append(e.replace(e, '-'))
//         elif e.isdigit():
//             new_strings.append(e)

//     print("".join(new_strings))


// # Sort Numbers - 7Kyu

// def solution(nums):
//     if nums:
//         return sorted(nums)
//     else:
//         return []


// print(solution([1, 2, 3, 10, 5]))


// # String Merge! - 7Kyu

// def string_merge(string1, string2, letter):
//     res = string1[:string1.index(letter)] + string2[string2.index(letter):]
//     return res


// print(string_merge("hello", "world", "l"))


// # Credit Card Mask - 7Kyu

// # return masked string
// def maskify(cc):
//     if len(cc) >= 4:
//         last_four_if_aval = cc[-4:]
//         sub_str = (len(cc) - 4) * '#'
//         return sub_str + last_four_if_aval

//     elif len(cc) < 4 and len(cc) > 0:
//         return cc

//     else:
//         return ''


// print(maskify("4556364607935616"))


// # Form The Minimum - 7Kyu

// def min_value(digits):
//     return int("".join(map(str, sorted(set(digits)))))


// print(min_value([1, 3, 1]))


// # Testing 1-2-3 - 7Kyu

// def number(lines):
//     numbered_lines = []
//     for n, text in enumerate(lines):
//         numbered_lines.append(str(n + 1) + ": " + text)

//     return numbered_lines


// print(number(["a", "b", "c"]))


// # Lost number in number sequence - 7Kyu


// def find_deleted_number(arr, mixed_arr):
//     if len(arr) != len(mixed_arr):
//         print(set(arr))
//         print(set(mixed_arr))
//         num_dif = list(set(arr) - set(mixed_arr))

//         return int("".join(str(e) for e in num_dif))
//     else:
//         return 0


// print(find_deleted_number([1, 2, 3, 4, 5], [3, 4, 1, 5]))


// # Combine objects - 7Kyu
// def combine(*args):
//     comb = {}
//     for i in args:
//         for k, v in i.items():
//             if k in comb:
//                 comb[k] += v
//             else:
//                 comb[k] = v
//     return comb


// print(combine({'a': 10, 'b': 20, 'c': 30}, {'a': 3, 'c': 6, 'd': 3}))

// """
// The items() method returns a view object. The view object contains the k-v pairs of the dictionary, as tuples in a list.
// The view object will reflect any changes done to the dictionary.
// """


// # 16+18=214 7Kyu

// def add(num1, num2):
//     odd_one = []
//     sum_nums = []

//     one = [int(i) for i in str(num1)]
//     two = [int(i) for i in str(num2)]

//     if len(one) < len(two):
//         len_dif = int(len(two) - len(one))
//         d = two[:len_dif]
//         temp_list = two[len_dif:]
//         sum_nums += [sum(pair) for pair in zip(temp_list, one)]
//         string_ints = [str(int) for int in d] + [str(int) for int in odd_one] + [str(int) for int in sum_nums]
//         str_of_ints = int("".join(string_ints))
//         return str_of_ints

//     elif len(one) > len(two):
//         len_dif = int(len(one) - len(two))
//         d = one[:len_dif]
//         temp_list = one[len_dif:]
//         sum_nums += [sum(pair) for pair in zip(temp_list, two)]
//         string_ints = [str(int) for int in d] + [str(int) for int in odd_one] + [str(int) for int in sum_nums]
//         str_of_ints = int("".join(string_ints))
//         return str_of_ints
//     else:
//         sum_nums += [sum(pair) for pair in zip(one, two)]
//         string_ints = [str(int) for int in sum_nums]
//         str_of_ints = int("".join(string_ints))
//         return str_of_ints


// print(add(122, 81))


// def area_or_perimeter(l, w):
//     if l == w:
//         return l * w
//     else:
//         return l * 2 + w * 2


// print(area_or_perimeter(3, 3))


// # Baby shark lyrics generator - 7Kyu
// # Create a function, as short as possible, that returns baby shark lyrics.


// def baby_shark_lyrics():
//     d = ' doo' * 6
//     prs = ['Baby ', 'Mommy ', 'Daddy ', 'Grandma ', 'Grandpa ']
//     s = ""
//     for p in prs:
//         s += (p + 'shark,' + d + '\n') * 3 + (p + 'shark!\n')
//     return s + ("Let's go hunt," + d + '\n') * 3 + ("Let's go hunt!\n") + "Run away,…"


// print(baby_shark_lyrics())

// # Slice the middle of a list backwards - 7Kyu
// """Write a function that takes a list of at least four elements as an argument and
// returns a list of the middle two or three elements in reverse order."""


// def reverse_middle(lst):
//     middle = int(len(lst) / 2)
//     nr_of_int_to_return = len(lst) - middle

//     non_reverse_list = lst[middle - 1:nr_of_int_to_return + 1]

//     reversed_list = non_reverse_list[::-1]

//     return reversed_list


// print("Reverse middle solution", reverse_middle([1, 2, 3, 4, 5]))

// # Remove the minimum - 7Kyu
// """Given an array of integers, remove the smallest value. Do not mutate the original array/list.
// If there are multiple elements with the same value, remove the one with a low"""


// def remove_smallest(numbers):
//     if numbers == []:
//         return []
//     else:
//         first_occurrence_of_min = numbers.index(min(numbers))
//         return numbers[:first_occurrence_of_min] + numbers[first_occurrence_of_min + 1:]


// print(remove_smallest([1, 2, 3, 1, 1]))

// # Sum the Repeats - 7Kyu
// # sum up all numbers that appear in two or more lists in the input list


// """The standard library provides the Python defaultdict type - a dictionary-like class
// behaves almost exactly like a regular Python dictionary, but if you try to access or modify a missing key,
// then defaultdict will automatically create the key and generate a default value for it.
// This makes defaultdict a valuable option for handling missing keys in dictionaries."""

// from collections import defaultdict


// def repeat_sum(l):
//     count = defaultdict(int)

//     for l1 in l:
//         for val in set(l1):
//             count[val] += 1

//     return sum(k for k, v in count.items() if v > 1)


// print("The sum is", repeat_sum([[1, 2], [2, 4], [3, 4, 4, 4], [123456789]]))


// # Sum of a nested list - 7Kyu
// def sum_nested(lst):
//     total = 0
//     for i in lst:
//         if isinstance(i, list):  # checks if `i` is a list
//             total += sum_nested(i)
//         else:
//             total += i
//     return total


// print("The sum of this nested list is:", sum_nested([1, [1], [[1]], [[[1]]]]))


// # Duplicate sandwich - 7Kyu
// def duplicate_sandwich(arr):
//     start, end = [i for i, x in enumerate(arr) if arr.count(x) > 1]
//     print(start)
//     print(end)
//     return arr[start + 1:end]


// print(duplicate_sandwich([0, 1, 2, 3, 4, 5, 6, 1, 7, 8]))



// from collections import defaultdict


// def repeat_sum(l):
//     count = defaultdict(int)
//     for l1 in l:
//         for val in set(l1):
//             count[val] += 1

//     return sum(k for k, v in count.items() if v > 1)


// #  Disorganised page lists - 7Kyu

// #  return an array with numbers that are out of place

// def find_page_number(pages):
//     n, miss = 1, []  # set n to 1 and an empty array miss for misplaced numbers

//     for i in pages:
//         if i != n:
//             miss.append(i)
//         else:
//             n += 1
//     return miss


// print(find_page_number([1, 2, 10, 3, 4, 5, 8, 6, 7]))


// #  Map over a list of lists - 7Kyu
// #  Write a function which maps a function over the lists in a list

// def grid_map(lst, op):  # which performs op(element) for all elements of lst
//     return [[*map(op, x)] for x in lst]


// # A List Comprehension follows the basic pattern:
// # [ <do something to item>  for  <item> in <list>]

// char_grid = [['h', 'E', 'l', 'l', 'O'], ['w', 'O', 'r', 'L', 'd']]
// print(grid_map(char_grid, lambda x: x.upper()))


// # Dictionary from two lists - 7Kyu

// #  1. return a dict from a list of keys and a list of values
// #  2. if there are not enough values, the keys for these values should be None
// #  3. if there are not enough keys, these values should be ignored.

// def createDict(keys, values):
//     if len(keys) > len(values):
//         values += (len(keys) - len(values)) * [None]
//         #  zip(keys, values)  # get pairs of elements
//         #  dict(zip(keys, values))  # convert to dictionary
//     return dict(zip(keys, values))  # return dictionary


// print(createDict(['a', 'b', 'c', 'd'], [1, 2, 3]))
// print(createDict(['a', 'b', 'c'], [1, 2, 3, 4]))


// # Isograms - 7Kyu
// def is_isogram(string):
//     unique_len = len(set(string.lower()))
//     if unique_len < len(string):
//         return False
//     else:
//         return True


// print("Is this string an isogram? ", is_isogram('aba'))
// print("Is this string an isogram? ", is_isogram('Dermatoglyphics'))


// # Unique Sum - 7Kyu
// def unique_sum_1(lst):
//     return sum(set(lst)) if lst else None


// print("The unique sum of the numbers in a given list is: ", unique_sum_1([2, 3, 3, 3]))


// def unique_sum_2(lst):
//     return sum(list(dict.fromkeys(lst))) if lst else None


// print("The unique sum of the numbers in a given list is: ", unique_sum_2([2, 3, 3, 3, 6, 666, 666]))


// # Max diff - easy - 7Kyu
// def max_diff(lst):
//     if len(lst) != 0:
//         return max(lst) - min(lst)
//     else:
//         return 0


// print("The difference is", max_diff([1, 2, 3, -4]))
