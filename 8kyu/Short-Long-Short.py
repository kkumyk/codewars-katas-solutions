def solution(a, b):
    one = len(a)
    two = len(b)
    if one > two:
        return b + a + b
    else:
        return a + b + a


print(solution('lkc2UNSf', 'MrdjiNI0DA'))
