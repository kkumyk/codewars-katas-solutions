/*
Given a non-negative integer n, write a function to_binary/ToBinary which returns that number in a binary format.
*/

function toBinary(n) {
    return parseInt(n.toString(2)); // Convert a number to a string, using base 2 (binary):
}

console.log(toBinary(5)); // should return 101;