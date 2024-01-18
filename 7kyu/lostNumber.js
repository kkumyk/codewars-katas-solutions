/*
An ordered sequence of numbers from 1 to N is given.
One number might have deleted from it, then the remaining numbers were mixed.
Find the number that was deleted.
*/

function findDeletedNumber(arr, mixArr) {

    let arrSum = arr.reduce((a, b) => a + b, 0);
    let mixArrSum = mixArr.reduce((a, b) => a + b, 0);

    return arrSum - mixArrSum;
}


console.log(findDeletedNumber([1, 2, 3, 4, 5], [3, 4, 1, 5])) // 2


