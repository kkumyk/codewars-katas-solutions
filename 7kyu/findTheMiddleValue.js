/*
As a part of this Kata, you need to create a function that when provided with a triplet,
returns the index of the numerical element that lies between the other two elements.
*/

function gimme(triplet) {
    return [...triplet].indexOf(triplet.sort((a, b) => a - b)[1]);
}

console.log(gimme([5, 10, 14])) // should return 1