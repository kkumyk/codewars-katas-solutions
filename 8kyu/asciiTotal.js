// # ASCII Total
// def uni_total(s):
//     sum = 0
//     for l in s:
//         sum += ord(l)
//     return sum

/*
You'll be given a string, and have to return the sum of all characters as an int.
The function should be able to handle all printable ASCII characters.
*/

function uniTotal(string) {
    let sum = 0;

    for (let i = 0; i < string.length; i++) {

        sum += string.charCodeAt(i)
    }

    return sum;

}

console.log(uniTotal("Mary Had A Little Lamb")) // should return 1873