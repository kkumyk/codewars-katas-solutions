/*
Reverse and invert all integer values in a given list.
reverse_invert([1,12,'a',3.4,87,99.9,-42,50,5.6]) = [-1,-21,-78,24,-5]
Remove all types other than integer.
*/

function reverseInvert(array) {
    let result = [];
    let filteredArray = array.filter((e) => typeof e === "number");
    let positiveNums = filteredArray
                            .filter((e) => typeof e === "number")
                            .map(e => (e * -1).toString().replace("-", ""))
                            .map(e => parseInt(String(e).split("").reverse().join("")));

    return positiveNums
}
console.log(reverseInvert([-9, "a", -18, 99, -10])) // [9,81,-99,1]