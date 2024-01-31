import math

def cooking_time(eggs):
    batches = math.ceil(eggs / 8)

    return batches * 5

print(cooking_time(20))  # 15
