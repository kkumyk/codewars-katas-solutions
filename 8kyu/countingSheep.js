/*
Consider an array/list of sheep where some sheep may be missing from their place.
We need a function that counts the number of sheep present in the array (true means present).
*/

// Solution 1
function countSheeps(sheep) {
    return sheep.filter(i => i === true).length;
}

// Solution 2
function countSheeps(sheep) {
    return sheep.filter(Boolean).length;
}

// Solution 3
function countSheeps(sheep) {
    return sheep.reduce((a, b) => a + (b === true ? 1 : 0), 0)
}


console.log(countSheeps([undefined, null, false, true])) // should return 1