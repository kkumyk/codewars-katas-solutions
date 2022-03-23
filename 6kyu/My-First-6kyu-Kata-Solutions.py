# Pair of gloves

from collections import Counter

def number_of_pairs(gloves):
    counts = Counter(gloves)
    x = counts.most_common()
    return round(sum([v - 1 for k, v in x if v % 2] + [v for k, v in x if v % 2 == 0]) / 2)


print(number_of_pairs(["red", "red", "red", "red", "red", "blue", "green", "green"]))

# Unique Strings
import itertools

def uniq_count(s):
    permutations = itertools.permutations(s.upper())
    unique_num = len(set("".join(permutation) for permutation in permutations))
    return unique_num


print(uniq_count("ABBb"))


# Detect Pangram
import string
import re


def is_pangram(s):
    alphanumeric_filter = filter(str.isalnum, s)
    alphanumeric_string = "".join(re.findall("[a-zA-Z]+", s)).lower()
    alphanumeric_string_no_duplicates = list(dict.fromkeys(alphanumeric_string))
    if len(alphanumeric_string_no_duplicates) == 26:
        return True
    else:
        return False


print(is_pangram("The quick, brown fox jumps over the lazy dog!"))

# Your order, please

def order(sentence):
    if sentence != "":
        words = sentence.split()
        remove_letters = [''.join(filter(str.isdigit, x)) for x in sentence if x]
        numbers = [x for x in remove_letters if x]
        sum_lists = sorted([a + b for a, b in zip(numbers, words)])
        for s in sum_lists:
            sum_lists_minus_num = [i[1:] for i in sum_lists]
        return " ".join(sum_lists_minus_num)
    else:
        return ""

print(order("is2 Thi1s T4est 3a"))

# Find The Parity Outlier
def find_outlier(integers):
    even = list(filter(lambda num: num % 2 == 0, integers))
    odd = list(filter(lambda num: num % 2 != 0, integers))

    if len(even) == 1:
        return even[0]
    else:
        return odd[0]

# Who likes it?
def likes(names):
    if len(names) == 0:
        return "no one likes this"

    elif len(names) == 1:
        return str(names[0]) + " likes this"

    elif len(names) == 2:
        return str(names[0]) + " and " + str(names[1]) + " like this"

    elif len(names) == 3:
        return str(names[0]) + ", " + str(names[1]) + " and " + str(names[2]) + " like this"

    else:
        return str(names[0]) + ", " + str(names[1]) + " and " + str(len(names) - 2) + " others like this"


# Bit Counting
def count_bits(n):
    binary = f'{n:08b}'
    return binary.count('1')

# Replace With Alphabet Position


