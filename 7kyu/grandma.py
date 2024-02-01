# replace "two", "too" and "to" with 2

import re

# re.sub() function returns a string where all matching occurrences
# of the specified pattern are replaced by the replaced string

def textin(s):
    return re.sub("(two|too|to)", "2", s, flags=re.IGNORECASE)


print(textin("Tomorrow send to her two text too."))
