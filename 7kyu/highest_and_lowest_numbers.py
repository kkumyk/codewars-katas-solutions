# // given a string of space separated numbers, and have to return the highest and lowest number;

# function highAndLow(numbers) {

#     numbersArray = numbers.split(" ").sort((a, b) => b - a);

#     return numbersArray[0] + " " + numbersArray.pop();
# }


def high_and_low(numbers):
    
    numbers = numbers.split(" ")
    result = []
    for s in numbers:
        result.append(int(s))
        
    return str(sorted(result)[-1]) + " " + str(sorted(result)[0])

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))  # "42 -9"
