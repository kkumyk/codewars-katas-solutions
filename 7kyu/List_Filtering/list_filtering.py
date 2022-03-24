"""
List Filtering

In this kata you will create a function that takes a list of non-negative integers and
strings and returns a new list with the strings filtered out.
"""


def filter_list(my_list):
    return [e for e in my_list if type(e) == int]
