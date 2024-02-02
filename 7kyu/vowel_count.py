
# - return the number (count) of vowels in the given string.
# - a, e, i, o, u are vowels but not y.
# - the input string will only consist of lower case letters and/or spaces.

def getCount(str):

    return sum(1 for vowel in str if vowel in "aeuioAEUIO")

print(getCount("abracadabra")) # 5