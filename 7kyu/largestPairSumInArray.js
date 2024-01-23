/*
Given a sequence of numbers, find the largest pair sum in the sequence.
*/

function largestPairSum(numbers) {

    return numbers.sort((a, b) => a - b).slice(-2).reduce((acc, curr) => acc + curr, 0);
}

console.log(largestPairSum([10, 14, 2, 23, 19])) // 42