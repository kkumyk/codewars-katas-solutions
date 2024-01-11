/*
Given the triangle of consecutive odd numbers calculate the sum of the numbers in the nth row of this triangle (starting at index 1).
*/

function rowSumOddNumbers(n) {
    return n * n * n;
}

console.log(rowSumOddNumbers(42)) // should return 74088