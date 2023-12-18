/*
Create a function that accepts a list/array and a number n, and returns a list/array of the first n elements from the list/array.
https://www.codewars.com/kata/56b1f01c247c01db92000076/solutions/javascript
*/

function doubleChar(str) {

    let result = ""

    for (let i = 0; i < str.length; i++) {
        result += str[i].repeat(2)
    }

    return result;
}

console.log(doubleChar("Adidas")) // should return "AAddiiddaass"