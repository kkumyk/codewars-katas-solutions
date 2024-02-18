# Your task is simply to count the total number of lowercase letters in a string.

import re

def lowercase_count(str):
    return len(re.findall('[a-z]',str))

# def lowercase_count(str):
#     return len(re.sub('[^a-z]', '', str))


print(lowercase_count("abc")) # 3