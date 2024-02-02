# - return the length of the shortest word(s).
# - string will never be empty and you do not need to account for different data types.

def find_short(s):

    return len(sorted(s.split(" "),key=len)[0])


def find_short(s):
     return min(len(w) for w in s.split())

print(find_short("bitcoin take over the world maybe who knows perhaps")) # 3