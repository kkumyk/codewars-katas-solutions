# Fix your code before the garden dies! - 8Kyu

def rain_amount(mm):
    if mm < 40:
        water_needed = 40 - int(mm)
        return "You need to give your plant " + str(water_needed) + "mm of water"
    else:
        return "Your plant has had more than enough water for today!"


# Plural

def plural(n):
    if n >= 2:
        return True
    elif n == 0:
        return True
    else:
        return False


# Name Your Python!

class Python:
    def __init__(self, name):
        self.name = name


# Unusual Five

def unusual_five():
    return len("five!")


# Drink about

def people_with_age_drink(age):
    if age < 14:
        return "drink toddy"
    elif age < 18:
        return "drink coke"
    elif age < 21:
        return "drink beer"
    else:
        return "drink whisky"



# Can we divide it?

def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        return True
    else:
        return False



# What is between?
def between(a, b):
    result = []
    for n in range(a, b + 1):
        result.append(n)
    return result


# Count Odd Numbers below n
def odd_count(n):
    return int(n / 2)

print(odd_count(23463634562))


# ASCII Total
def uni_total(s):
    sum = 0
    for l in s:
        sum += ord(l)
    return sum


# Check same case

def same_case(a, b):
    if a.isalpha() != True or b.isalpha() != True:
        return -1
    elif a == a.lower() and b == b.lower():
        return 1
    elif a != a.lower() and b != b.lower():
        return 1
    else:
        return 0


# Multiplication table for number
def multi_table(number):
    nums_to_mult = []
    for i in range(1, 11):
        nums_to_mult.append(str(i) + ' * {}'.format(str(number)))

    nums = []
    for s in nums_to_mult:
        nums.append(s[:2].rstrip())

    answers = []
    for a in nums:
        answers.append(int(a[:2]) * number)

    res = nums_to_mult[0] + ' = ' + str(answers[0]) + '\n' + nums_to_mult[1] + ' = ' + str(answers[1]) + '\n' + \
          nums_to_mult[2] + ' = ' + str(answers[2]) + '\n' + nums_to_mult[3] + ' = ' + str(answers[3]) + '\n' + \
          nums_to_mult[4] + ' = ' + str(answers[4]) + '\n' + nums_to_mult[5] + ' = ' + str(answers[5]) + '\n' + \
          nums_to_mult[6] + ' = ' + str(answers[6]) + '\n' + nums_to_mult[7] + ' = ' + str(answers[7]) + '\n' + \
          nums_to_mult[8] + ' = ' + str(answers[8]) + '\n' + nums_to_mult[9] + ' = ' + str(answers[9])
    return res


# Return Two Highest Values in List
def two_highest(arg1):
    sorted_list = sorted(arg1, reverse=True)
    unique_list_values = list(dict.fromkeys(sorted_list))

    return unique_list_values[0:2]


# Define a card suit
def define_suit(card):
    res = ''
    if card[-1].lower() == 'c':
        res += 'clubs'
    elif card[-1].lower() == 'd':
        res += 'diamonds'
    elif card[-1].lower() == 'h':
        res += 'hearts'
    elif card[-1].lower() == 's':
        res += 'spades'
    return res


# Twice as old

def twice_as_old(dad_years_old, son_years_old):
    double_age = son_years_old * 2
    years = dad_years_old - double_age

    if years > 0:
        return years
    else:
        return double_age - dad_years_old


# a better solution would be to use abs() function which returns the absolute value of a number
def twice_as_old_update(dad_years_old, son_years_old):
    return abs(dad_years_old - 2 * son_years_old)


# Parse nice int from char problem
def get_age(age):
    chars = []
    for char in age:
        chars.append(char)
        return int(age[0])


# Calculate BMI
def bmi(weight, height):
    bmi = weight / (height * height)
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25.0:
        return "Normal"
    elif bmi <= 30.0:
        return "Overweight"
    else:
        return "Obese"


# Fake Binary
def fake_bin(x):
    res = ""
    for n in x:
        if int(n) < 5:
            res += str(0)
        else:
            res += str(1)
    return res


# Beginner Series #1 School Paperwork

def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m


def paperwork_update(n, m):
    return n * m if n > 0 and m > 0 else 0


# A Needle in the Haystack
def find_needle(haystack):
    for n in haystack:
        if n == 'needle':
            # he index() method returns the position at the first occurrence
            # of the specified value.
            return 'found the needle at position ' + str(haystack.index('needle'))

print(find_needle(['hay', 'junk', 'hay', 'hay', 'moreJunk', 'needle', 'randomJunk']))


# Convert number to reversed array of digits
def digitize(n):
    string_list = []
    for i in str(n):
        string_list += i

    # The map() function executes a specified function for each item in an iterable.
    # The item is sent to the function as a parameter.
    # map(function, iterables)
    integer_map = map(int, string_list)  # the map f turns each str in the list into integer
    integer_list = list(integer_map)
    # Reverse a List Using Slicing Operator [::-1]
    return integer_list[::-1]


def digitize_update(n):
    return list(map(int, str(n)[::-1]))

print(digitize_update(35231))


# Grasshopper - Summation

def summation(num):
    sum = 0
    # Create a sequence of numbers, starting from 1 to num+1 with the range() function
    # as an integer number specifying at which position to stop will be not included.
    # The range function increments by 1 (by default).

    for i in range(1, num + 1):
        sum += i

    return sum


# Remove duplicates from list
def distinct(seq):
    return list(dict.fromkeys(seq))

print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))


# Calculate average
def find_average(numbers):
    return sum(numbers) / len(numbers)


# Returning Strings
def greet(name):
    return "Hello, " + name + " how are you doing today?"


# Vowel remover
def shortcut(s):
    vowels = ['a', 'o', 'i', 'u', 'e']
    amended_s = ''
    for char in s:
        if char in vowels:
            amended_s += ''
        else:
            amended_s += char
    return amended_s


# Sum The Strings
def sum_str(a, b):
    if a == '' and b == '':
        return str(0)
    elif a == '':
        return b
    elif b == '':
        return a
    else:
        sum_int = int(a) + int(b)
        return str(sum_int)