/*
Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).
If they are, change the array value to a string of that vowel.
Return the resulting array.
*/

function isVow(a) {

    let result = [];

    for (let i = 0; i < a.length; i++) {

        if ('aeiou'.indexOf(String.fromCharCode(a[i])) !== -1) {
            result.push(String.fromCharCode(a[i]))
        } else {
            result.push(a[i])
        }
    }
    return result;
}

console.log(isVow([101, 121, 110, 113, 113, 103, 121, 121, 101, 107, 103]))