def spin_words(sentence):
    rev = []
    res = sentence.split()
    for w in res:
        if len(w) >= 5:
            rev.append(w[::-1])
        else:
            rev.append(w)
    return ' '.join(rev)
