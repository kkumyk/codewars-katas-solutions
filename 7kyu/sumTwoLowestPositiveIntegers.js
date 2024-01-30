
function sumTwoSmallestNumbers(numbers) {
    return numbers.sort((a, b) => a - b).slice(0, 2).reduce((a, b) => a + b, 0);
}


console.log(sumTwoSmallestNumbers([19, 5, 42, 2, 77])) // 7