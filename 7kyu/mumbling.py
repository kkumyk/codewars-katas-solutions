# This time no story, no theory. The examples below show you how to write function accum:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"


def accum(st):
    newArr = []
    arr = [l.lower() for l in st]

    for idx, letter in enumerate(arr):
        subString = ""
        subString += arr[idx].upper()
        subString += (arr[idx] * (idx + 1))[0:-1]
        newArr.append(subString)
    return "-".join(newArr)


print(accum("mumbling"))
