/*Simply find the closest value to zero from the list. Notice that there are negatives in the list.*/

function closest(arr) {

    let sorted = arr.sort((x, y) => Math.abs(x) - Math.abs(y)); // [ -1, 2, -3, 4 ]
    
    let positiveNums = [...new Set(arr.map(n => Math.abs(n)))]
    console.log(sorted)
    console.log(positiveNums)

    if (sorted.length !== positiveNums.length) {
        return null
    } else if (arr.includes(0)) {
        return 0
    } else {
        return sorted[0];
    }
}
console.log(closest([5, 1, -1, 2, -10])) // -1