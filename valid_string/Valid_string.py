def valid_word(seq, word):
    if word == "":
        return True
    for x in range(len(word) + 1):
        if word[:x] in seq and valid_word(seq, word[x:]):
            return True
    return False


print(valid_word(['code', 'wars'], 'codewars'))
print(valid_word(['code', 'war'], 'codewars'))
