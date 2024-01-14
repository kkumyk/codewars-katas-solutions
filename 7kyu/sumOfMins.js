/*
Given a 2D ( nested ) list ( array, vector, .. ) of size m * n,
your task is to find the sum of the minimum values in each row.
*/

function sumOfMinimums(arr) {

    let result = [];

    for (let i = 0; i < arr.length; i++) {
        result.push(arr[i].sort((a, b) => a - b)[0])
    }
    return result.reduce((a, b) => a + b, 0);
}

console.log(sumOfMinimums([[7, 9, 8, 6, 2], [6, 3, 5, 4, 3], [5, 8, 7, 4, 5]])) // should return 9