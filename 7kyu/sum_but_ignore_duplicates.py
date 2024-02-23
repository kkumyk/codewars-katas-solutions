def sum_no_duplicates(l):
    result = 0

    for num in l:
        if l.count(num) == 1:
            result += num

    return result


print(sum_no_duplicates([3, 4, 3, 6]))  # 10
