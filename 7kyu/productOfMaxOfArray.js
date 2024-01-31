function maxProduct(numbers, size) {

    return numbers.sort((a, b) => b - a).slice(0, size).reduce((a, b) => a * b, 1)
}


console.log(maxProduct([10,8,7,9], 3)) // 720