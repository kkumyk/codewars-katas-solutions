/*
Write a function which takes a list of strings and returns each line prepended by the correct number.
*/

let number = function (array) {
    let result = [];

    for (let i = 1; i <= array.length; i++) {
        result.push(String(i)  + ": " + array[i-1])
    }

    return result;
}

console.log(number(["a", "b", "c"])) // ["1: a", "2: b", "3: c"]