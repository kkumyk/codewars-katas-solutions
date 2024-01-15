/*
In this kata you get the start number and the end number of a region and 
should return the count of all numbers except numbers with a 5 in it.
The start and the end number are both inclusive!
*/

// Solution 1
function dontGiveMeFive(start, end) {
    let result = [];

    for (let i = start; i <= end; i++) {
        if ((!String(i).split("").includes("5"))) {
            result.push(i)
        }
    }
    return result.length;
}

console.log(dontGiveMeFive(4, 17)) // should return 12

// Solution 2
function dontGiveMeFive(start, end) {

    // "_" indicates an unused parameter; it's a common practice to assign unused parameters to the "_"
    // map() will not call for unassigned element. This mean we need to initialise the new Array(n) before mapping.
    // One standard technique is to use fill. 
    let range = (new Array(end - start + 1)).fill(undefined).map((_, i) => i + start);

    let result = []
    let test = []

    for (let el of range) { test.push(el.toString().split("")) }

    for (let ar of test) {
        if (ar.includes("5")) {
            ar++
        } else { result.push(ar) }
    }
    return result.length

}