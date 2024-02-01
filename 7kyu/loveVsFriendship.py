# write a function which calculates the value of a word based of the sum of the alphabet positions

# ord() returns the number representing the unicode of a specific character


def words_to_marks(s):
    sum = 0
    for u in s:
        sum += ord(u) - 96
    return sum


print(words_to_marks("love"))
