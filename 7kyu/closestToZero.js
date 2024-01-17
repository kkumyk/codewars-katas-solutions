/*Simply find the closest value to zero from the list. Notice that there are negatives in the list.*/

function closest(arr) {

    if (arr.includes(0)) {
        return 0
    }

    let sorted = arr.sort((x, y) => Math.abs(x) - Math.abs(y)); // [ 1, -1, 2, 5, -10 ]
    
    for (let i = 0; i <= arr.length; i++) {
        if (arr.includes(sorted[0] * -1)) { // checks if the opposite number is in the original array;
            return null;
        } return sorted[0];
    }
}
console.log(closest([5, 1, -1, 2, -10])) //null