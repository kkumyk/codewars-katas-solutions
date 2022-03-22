# Lario and Muigi Pipe Problem - 8Kyu
def pipe_fix(nums):
    res = []
    for n in range(min(nums), max(nums) + 1):
        res.append(n)

    return res