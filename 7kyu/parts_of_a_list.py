# https://www.codewars.com/kata/56f3a1e899b386da78000732/

def part_list(arr):
    
    new_arr = []
    for x in range(1,len(arr)):
        y = " ".join(arr[:x])
        z = " ".join(arr[x:])
        new_arr.append((y,z))
    return new_arr

print(part_list( ["az", "toto", "picaro", "zone", "kiwi"]))