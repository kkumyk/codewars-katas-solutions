/*
Given an input of an array of digits, return the array with each digit incremented by its position in the array:
the first digit will be incremented by 1, the second digit by 2, etc.
Make sure to start counting your positions from 1 ( and not 0 ).
*/

function incrementer(num) {
    return num.map((n, i) => (n + i + 1) % 10);
}

console.log(incrementer([4, 6, 7, 1, 3])) // should return [5, 8, 0, 5, 8]