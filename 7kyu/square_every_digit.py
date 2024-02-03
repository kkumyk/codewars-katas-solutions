def square_digits(num):
    res = ""
    for n in str(num):
        res += str(int(n) ** 2)
    return int(res)
