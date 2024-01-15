/*
Reverse and invert all integer values in a given list.
reverse_invert([1,12,'a',3.4,87,99.9,-42,50,5.6]) = [-1,-21,-78,24,-5]
Remove all types other than integer.
*/

function reverseInvert(array) {
    result = [];
    for (el of array)
        if (Number.isInteger(el)) { // determines whether the passed value is an integer
            if (el < 0) {
                result.push(Number(Math.abs(el).toString().split('').reverse().join('')));
            }
            else { result.push(-Number(el.toString().split('').reverse().join(''))); }
        }
    return result;
}
console.log(reverseInvert([-9, "a", -18, 99, -10])) // [9,81,-99,1]