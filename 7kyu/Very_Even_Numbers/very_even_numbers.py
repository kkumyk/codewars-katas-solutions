"""
"Very Even" Numbers
Write a function that returns true if the number is a "Very Even" number.
If a number is a single digit, then it is simply "Very Even" if it itself is even.
If it has 2 or more digits, it is "Very Even" if the sum of its digits is "Very Even".

Examples:
number = 88 => returns false -> 8 + 8 = 16 -> 1 + 6 = 7 => 7 is odd
number = 222 => returns true -> 2 + 2 + 2 = 6 => 6 is even
"""


def is_very_even_number(n):
    if n <= 9:
        return n % 2 == 0
    else:
        num = 0
        n = str(n)
        for digit in n:
            num += int(digit)
        return is_very_even_number(num)

print(is_very_even_number(848))
