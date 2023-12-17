// # Fix your code before the garden dies! - 8Kyu

// def rain_amount(mm):
//     if mm < 40:
//         water_needed = 40 - int(mm)
//         return "You need to give your plant " + str(water_needed) + "mm of water"
//     else:
//         return "Your plant has had more than enough water for today!"


// # Plural

// def plural(n):
//     if n >= 2:
//         return True
//     elif n == 0:
//         return True
//     else:
//         return False


// # Name Your Python!

// class Python:
//     def __init__(self, name):
//         self.name = name


// # Unusual Five

// def unusual_five():
//     return len("five!")


// # Drink about

// def people_with_age_drink(age):
//     if age < 14:
//         return "drink toddy"
//     elif age < 18:
//         return "drink coke"
//     elif age < 21:
//         return "drink beer"
//     else:
//         return "drink whisky"



// # Can we divide it?

// def is_divide_by(number, a, b):
//     if number % a == 0 and number % b == 0:
//         return True
//     else:
//         return False



// # What is between?
// def between(a, b):
//     result = []
//     for n in range(a, b + 1):
//         result.append(n)
//     return result


// # Count Odd Numbers below n
// def odd_count(n):
//     return int(n / 2)

// print(odd_count(23463634562))


// # ASCII Total
// def uni_total(s):
//     sum = 0
//     for l in s:
//         sum += ord(l)
//     return sum


// # Check same case

// def same_case(a, b):
//     if a.isalpha() != True or b.isalpha() != True:
//         return -1
//     elif a == a.lower() and b == b.lower():
//         return 1
//     elif a != a.lower() and b != b.lower():
//         return 1
//     else:
//         return 0


// # Multiplication table for number
// def multi_table(number):
//     nums_to_mult = []
//     for i in range(1, 11):
//         nums_to_mult.append(str(i) + ' * {}'.format(str(number)))

//     nums = []
//     for s in nums_to_mult:
//         nums.append(s[:2].rstrip())

//     answers = []
//     for a in nums:
//         answers.append(int(a[:2]) * number)

//     res = nums_to_mult[0] + ' = ' + str(answers[0]) + '\n' + nums_to_mult[1] + ' = ' + str(answers[1]) + '\n' + \
//           nums_to_mult[2] + ' = ' + str(answers[2]) + '\n' + nums_to_mult[3] + ' = ' + str(answers[3]) + '\n' + \
//           nums_to_mult[4] + ' = ' + str(answers[4]) + '\n' + nums_to_mult[5] + ' = ' + str(answers[5]) + '\n' + \
//           nums_to_mult[6] + ' = ' + str(answers[6]) + '\n' + nums_to_mult[7] + ' = ' + str(answers[7]) + '\n' + \
//           nums_to_mult[8] + ' = ' + str(answers[8]) + '\n' + nums_to_mult[9] + ' = ' + str(answers[9])
//     return res


// # Return Two Highest Values in List
// def two_highest(arg1):
//     sorted_list = sorted(arg1, reverse=True)
//     unique_list_values = list(dict.fromkeys(sorted_list))

//     return unique_list_values[0:2]


// # Define a card suit
// def define_suit(card):
//     res = ''
//     if card[-1].lower() == 'c':
//         res += 'clubs'
//     elif card[-1].lower() == 'd':
//         res += 'diamonds'
//     elif card[-1].lower() == 'h':
//         res += 'hearts'
//     elif card[-1].lower() == 's':
//         res += 'spades'
//     return res


// # Twice as old

// def twice_as_old(dad_years_old, son_years_old):
//     double_age = son_years_old * 2
//     years = dad_years_old - double_age

//     if years > 0:
//         return years
//     else:
//         return double_age - dad_years_old


// # a better solution would be to use abs() function which returns the absolute value of a number
// def twice_as_old_update(dad_years_old, son_years_old):
//     return abs(dad_years_old - 2 * son_years_old)


// # Parse nice int from char problem
// def get_age(age):
//     chars = []
//     for char in age:
//         chars.append(char)
//         return int(age[0])


// # Calculate BMI
// def bmi(weight, height):
//     bmi = weight / (height * height)
//     if bmi <= 18.5:
//         return "Underweight"
//     elif bmi <= 25.0:
//         return "Normal"
//     elif bmi <= 30.0:
//         return "Overweight"
//     else:
//         return "Obese"


// # Fake Binary
// def fake_bin(x):
//     res = ""
//     for n in x:
//         if int(n) < 5:
//             res += str(0)
//         else:
//             res += str(1)
//     return res


// # Beginner Series #1 School Paperwork

// def paperwork(n, m):
//     if n < 0 or m < 0:
//         return 0
//     else:
//         return n * m


// def paperwork_update(n, m):
//     return n * m if n > 0 and m > 0 else 0


// # A Needle in the Haystack
// def find_needle(haystack):
//     for n in haystack:
//         if n == 'needle':
//             # he index() method returns the position at the first occurrence
//             # of the specified value.
//             return 'found the needle at position ' + str(haystack.index('needle'))

// print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))


// # Convert number to reversed array of digits
// def digitize(n):
//     string_list = []
//     for i in str(n):
//         string_list += i

//     # The map() function executes a specified function for each item in an iterable.
//     # The item is sent to the function as a parameter.
//     # map(function, iterables)
//     integer_map = map(int, string_list)  # the map f turns each str in the list into integer
//     integer_list = list(integer_map)
//     # Reverse a List Using Slicing Operator [::-1]
//     return integer_list[::-1]


// def digitize_update(n):
//     return list(map(int, str(n)[::-1]))

// print(digitize_update(35231))


// # Grasshopper - Summation

// def summation(num):
//     sum = 0
//     # Create a sequence of numbers, starting from 1 to num+1 with the range() function
//     # as an integer number specifying at which position to stop will be not included.
//     # The range function increments by 1 (by default).

//     for i in range(1, num + 1):
//         sum += i

//     return sum


// # Remove duplicates from list
// def distinct(seq):
//     return list(dict.fromkeys(seq))

// print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))


// # Calculate average
// def find_average(numbers):
//     return sum(numbers) / len(numbers)


// # Returning Strings
// def greet(name):
//     return "Hello, " + name + " how are you doing today?"


// # Vowel remover
// def shortcut(s):
//     vowels = ['a', 'o', 'i', 'u', 'e']
//     amended_s = ''
//     for char in s:
//         if char in vowels:
//             amended_s += ''
//         else:
//             amended_s += char
//     return amended_s


// # Sum The Strings
// def sum_str(a, b):
//     if a == '' and b == '':
//         return str(0)
//     elif a == '':
//         return b
//     elif b == '':
//         return a
//     else:
//         sum_int = int(a) + int(b)
//         return str(sum_int)
    
    

// # Enumerable Magic #25 - Take the First N Elements - 8Kyu
// def take(arr, n):
//     return arr[0:n]

// # Remove First and Last Character - 8Kyu
// def remove_char(s):
//     return s[1:len(s) - 1]

// def remove_char_alternative(s):
//     return s[1:-1]

// # String to number - 8Kyu
// def string_to_number(s):
//     return int(s)

// # Double Char - 8Kyu
// def double_char(s):
//     new_string = ""
//     for char in s:
//         new_string += char*2
//     return new_string
// print(double_char("String"))



// # String repeat - 8Kyu
// def repeat_str(repeat, string):
//     return string * repeat
// print(repeat_str(4, 'a'))




// # Sum of positive - 8Kyu
// def positive_sum(arr):
//     sum_nums = 0
//     for n in arr:
//         if n > 0:
//             sum_nums += n
//     return sum_nums
// print(positive_sum([1, 2, 3, 4, 5]))

// def remove_consecutive_duplicates(s):
//     words = s.split(' ')
//     result = words[0] + ' '
//     for pos in range(1, len(words)):
//         if words[pos] != words[pos - 1]:
//             result += words[pos] + ' '
//     return result.strip()
// print(remove_consecutive_duplicates('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))

// def comes_after(st, l):
//     res = ''
//     for i, e in enumerate(st):
//         if e.lower() == l.lower() and i < len(st) - 1:
//             res += st[i + 1]
//     return ''.join([i for i in res if i.isalpha()])
// print(comes_after("Pirates say arrrrrrrrr.", 'r'))

// from math import copysign as sign
// def reverse_invert(lst):
//     return [-int(sign(int(str(abs(x))[::-1]), x)) for x in lst if isinstance(x, int)]

// # Sum without highest and lowest number - 8Kyu
// def sum_array(arr):
//     if not arr:
//         return 0

//     elif arr:
//         sorted_arr = sorted(arr)

//         if len(sorted_arr) > 1:
//             sum_res = sorted_arr[1:-1]
//             return sum(sum_res)
//         elif len(sorted_arr) == 1:
//             return 0
//     else:
//         return 0
// print(sum_array([6, 2, 1, 8, 10]))

// # Difference of Volumes of Cuboids - 8kYU
// def find_difference(a, b):
//     x = a[0] * a[1] * a[2]
//     y = b[0] * b[1] * b[2]
//     return max(x, y) - min(x, y)
// print(find_difference([2, 2, 3], [5, 4, 1]))

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

// # Is it a palindrome? - 8Kyu
// def is_palindrome(s):
//     return s.lower() == s.lower()[::-1]
// print(is_palindrome('AAAAAAAAAAAAAAAAAAAAAAA'))

// # Is it even? - 8Kyu
// def is_even(n):
//     return (n % 2) == 0

// # Area or Perimeter - 8Kyu
// """You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
// If it is a square, return its area. If it is a rectangle, return its perimeter."""
// def area_or_perimeter(l, w):
//     if l == w:
//         return l * w
//     else:
//         return l * 2 + w * 2
// print(area_or_perimeter(3, 3))

// # String cleaning - 8Kyu
// def string_clean(s):
//     return ''.join([i for i in s if not i.isdigit()])
// print(string_clean('E3at m2e2!'))

// # repeatIt - 8Kyu
// # Create a function that takes a string and an integer (n).
// # The function should return a string that repeats the input string n number of times.
// # If anything other than a string is passed in you should return "Not a string"
// def repeat_it(string, n):
//     return string * n if type(string) == str else 'Not a string'
// print(repeat_it("*-*", 5))

// # Alternative solution using isinstance function which returns True if the specified object is of the specified type,
// # otherwise False:
// def repeat_it(string, n):
//     return string * n if isinstance(string, str) else 'Not a string'
// print(repeat_it("*^*", 5))



// from collections import defaultdict
// def repeat_sum(l):
//     count = defaultdict(int)
//     for l1 in l:
//         for val in set(l1):
//             count[val] += 1

//     return sum(k for k, v in count.items() if v > 1)
