/*
Write a function which takes a list of strings and returns each line prepended by the correct number.
*/

// Solution 1
let number = function (array) {
    let result = [];

    for (let i = 1; i <= array.length; i++) {
        result.push(String(i) + ": " + array[i - 1])
    }

    return result;
}

// Solution 2
let number2Solution = (array) => array.map((v, i) => `${i + 1}: ${v}`)

console.log(number(["a", "b", "c"])) // ["1: a", "2: b", "3: c"]

console.log(number2Solution(["a", "b", "c"])) // ["1: a", "2: b", "3: c"]