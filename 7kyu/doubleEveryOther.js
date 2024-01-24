/*
Write a function that doubles every second integer in a list, starting from the left.
*/

function doubleEveryOther(a) {
    return a.map((n, i) => i % 2 === 0 ? n : n * 2);
}

console.log(doubleEveryOther([1, 2, 3, 4])) // [1,4,3,8]