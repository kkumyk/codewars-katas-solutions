# grey dog   => blue dog

import re

"""
() grouping

. any single character except a newline

+ one or more of the preceding character

?= is a positive lookahead, saying is that the captured match must be followed by whatever is within the parentheses but that part isn't captured.

"""
search = ".+(?=(dog|cat))"
substitute = "blue"

str = "grey dog"
new_str = re.sub(r".+(?= (dog|cat))", "blue", str)

print(new_str)
