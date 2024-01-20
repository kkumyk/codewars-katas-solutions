/*
In this kata, you are asked to square every digit of a number and concatenate them.
*/

function squareDigits(num) {

    return parseInt(String(num).split("").map((n) => (Number(n) * Number(n))).join(""));
}

console.log(squareDigits(3212)) // 9414