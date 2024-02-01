
# - fn to split the chocolate bar of given dimension n x m into small squares;
# - each square is of size 1x1 and unbreakable;
# - write fn that will return minimum number of breaks:
#     - a bar of size 2 x 1 - one break
#     - a bar 3 x 1 - two breaks
# - if input data is invalid you should return 0


def break_chocolate (n, m):
    if n * m == 0:
        return 0 
    return n * m - 1

print(break_chocolate(5, 5)) # 24