/*
- input: an odd-length array of integers, in which all of them are the same, except for one
- output: a single different number
*/

function stray(numbers) {
    let sortedArray = numbers.sort((a, b) => a - b)
    return (sortedArray[0] === sortedArray[1]) ? sortedArray.pop() : sortedArray[0]
}


console.log(stray([1, 1, 1, 1, 4, 1, 1, 1]))