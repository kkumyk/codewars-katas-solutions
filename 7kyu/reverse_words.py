# Solution 1

def reverse_words(text):
    result = ""  #
    for word in text.split(" "):
        result += word[::-1] + " "

    return result.strip()


# Solution 2

def reverse_words(text):
    return " ".join(word[::-1] for word in text.split(" "))


print(reverse_words("quick brown fox"))  # "kciuq nworb xof"
