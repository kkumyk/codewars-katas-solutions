/*
Create a function that accepts a list/array and a number n, and returns a list/array of the first n elements from the list/array.
*/

function doubleChar(str) {

    let result = ""

    for (let i = 0; i < str.length; i++) {
        result += str[i].repeat(2)
    }

    return result;
}

console.log(doubleChar("Adidas")) // should return "AAddiiddaass"