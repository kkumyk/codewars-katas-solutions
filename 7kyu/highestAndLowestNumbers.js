// given a string of space separated numbers, and have to return the highest and lowest number;

function highAndLow(numbers) {

    numbersArray = numbers.split(" ").sort((a, b) => b - a);
    
    return numbersArray[0] + " " + numbersArray.pop();
}


console.log(highAndLow("8 3 -5 42 -1 0 0 -9 4 7 4 -4")) // "42 -9"