"""
Character Counter

You are going to be given a word. Your job will be to make sure that each character in that word has the exact same
number of occurrences. You will return true if it is valid, or false if it is not.

"""


def validate_word(word):
    new_list = sorted(list(word.lower()))
    char_counts = dict((i, new_list.count(i)) for i in new_list)
    count_values = char_counts.values()
    remove_duplicates = list(dict.fromkeys(count_values))
    if len(remove_duplicates) > 1:
        return False
    return True
