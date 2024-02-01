# return true if the first instance of "x" in the string is immediately followed by the string "xx"

# find() vs index() - index() method raises an exception if no values was found


def triple_x(str):
    idxOfX = str.find("x")
    three_chars = str[idxOfX : idxOfX + 3]
    return three_chars == "xxx"


print(tripleX("abraxxxcadabra"))  # true
