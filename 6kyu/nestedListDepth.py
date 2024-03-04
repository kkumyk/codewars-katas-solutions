"""
Write a function that determines the depth of the deepest nested list within a given list.
list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1]) >> 6
list_depth([2.0, [2, 0], 3.7, [3, 7], 6.7, [6, 7]]) >> 2
"""

def list_depth(l):
    
    if l == []:
        return 1
    if isinstance(l, list):
        return 1 + max(list_depth(item) for item in l)
    else:
        return 0

print(list_depth([1, [2, [3, [4, [5, [6], 5], 4], 3], 2], 1]))
