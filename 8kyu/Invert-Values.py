""""
Invert values

Given a set of numbers, return the additive inverse of each.
Each positive becomes negatives, and the negatives become positives.
invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
"""

# Solution from 17.12.2021

def invert(lst):
    new_lst = []

    for i in lst:
        if i < 0:
            new_lst.append(i * (-1))
        else:
            new_lst.append(i * (-1))
    return new_lst


# Solution from 28.03.2022

def invert(lst):
    new_list = []
    for item in lst:
        new_list.append(item * -1)
    return new_list
