# Find the missing letter - 6Kyu

def find_missing_letter(chars):
    alphabet_lower = "".join([chr(i) for i in range(ord('a'), ord('z') + 1)])
    alphabet = alphabet_lower + alphabet_lower.upper()
    first = alphabet.index(chars[0])
    last = alphabet.index(chars[-1])
    res = alphabet[first:last + 1] + ''.join(chars)
    return ''.join([c for c in res if res.count(c) == 1])


print(find_missing_letter(['a', 'b', 'c', 'd', 'f']))
print(find_missing_letter(['O', 'Q', 'R', 'S']))


# Find the unique number - 6Kyu

def find_uniq(arr):
    first = sorted(arr)[0]
    last = sorted(arr)[-1]
    if first == sorted(arr)[1]:
        return last
    else:
        return first


print(find_uniq([1, 1, 1, 2, 1, 1]))


# Count characters in your string - 6Kyu

def count(string):
    unique_chars = sorted(list(set(string)))
    counts = {}

    for k in unique_chars:
        counts[k] = string.count(k)
    return counts


print(count('aba'))


# Difference of 2 - 6Kyu

def twos_difference(arr):
    return [(i, i + 2) for i in sorted(arr) if i + 2 in arr]


print(twos_difference([1, 2, 3, 4]))


# Sort the odd - 6Kyu

def sort_array(source_array):
    odds_list = sorted([item for item in source_array if item % 2 != 0])
    odd_int = 0
    for i in range(len(source_array)):
        if source_array[i] % 2 != 0:
            source_array[i] = odds_list[odd_int]
            odd_int += 1
    return source_array


print(sort_array([5, 3, 2, 8, 1, 4]))


# Your order, please - 6Kyu

def order(sentence):
    res = ''
    for i in range(1, len(sentence)):
        for s in sentence.split():
            if str(i) in s:
                res += s + ' '
    return res.strip()


print(order("is2 Thi1s T4est 3a"))