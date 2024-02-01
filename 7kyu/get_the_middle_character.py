import math


def get_middle(s):
    x = len(s)  # 4
    y = int(x / 2)  # 2

    if x % 2 == 0:
        return s[y - 1 : y + 1]
    return s[y : y + 1]


print(get_middle("todo"))
