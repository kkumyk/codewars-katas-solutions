/*
Write a function that takes a list of at least four elements as an argument and returns a list of the middle two or three elements in reverse order.
*/

function reverseMiddle(array) {

    let listMiddle = Math.floor(array.length / 2) - 1; // 1
    return array.slice(listMiddle).reverse().slice(listMiddle);
}

console.log(reverseMiddle([1, 2, 3, 4, 5])) //  [ 4, 3, 2 ]