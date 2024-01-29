// fn to check if the numbers in array are in the ascending order

function isAscOrder(arr) {

    for (let i = 0; i < arr.length - 1; i++) { // move up to last number in the array
        if (arr[i] > arr[i + 1]) {
            return false;
        }
    }
    return true;
}

console.log(isAscOrder([1, 24, 6, 3, 77])) // false