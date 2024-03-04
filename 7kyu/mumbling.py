"""
Input > Output:
mumbling("abcd") -> "A-Bb-Ccc-Dddd"
mumbling("cwAt") -> "C-Ww-Aaa-Tttt"

1. turn all letters to lowercase and create a letters array;
2. iterate over the letters array and use * operator on each letter:
- arr[i] - accesses the letter in the array
- (i + 1) sets the number of repetition needed starting from 1

"""

# Solution 1

def mumbling(st):

    newArr = []
    arr = [l.lower() for l in st]

    for i, l in enumerate(arr):

        newArr.append(arr[i] * (i + 1))

    return "-".join(newArr).title()


print(mumbling("mum"))


# Solution 2

# def mumbling(st):
#     newArr = []
#     arr = [l.lower() for l in st]

#     for idx, letter in enumerate(arr):
#         subString = ""
#         subString += arr[idx].upper()
#         subString += (arr[idx] * (idx + 1))[0:-1]
#         newArr.append(subString)
#     return "-".join(newArr)
