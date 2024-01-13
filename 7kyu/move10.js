/*
Move every letter in the provided string forward 10 letters through the alphabet.
If it goes past 'z', start again at 'a'.
Input will be a string with length > 0.
*/

function moveTen(s) {
    /*[...Array(26).keys()] - returns an Array Iterator object with the keys of an array: 
    [0, 1, 2, 3 ...25]
    
    The String.fromCharCode()
    static method returns a string created from the specified sequence of UTF-16 code units.
    String.fromCharCode(97); returns "a"
    */
    let alphabet = [...Array(26).keys()].map(i => String.fromCharCode(i + 97)).join("");
    let moved10 = alphabet.slice(10) + alphabet.slice(0, 10);
    // alphabet:    abcdefghijklmnopqrstuvwxyz
    // moved10:     klmnopqrstuvwxyzabcdefghij

    return s.replace(/[a-z]/g, x => moved10[alphabet.indexOf(x)]);
}

console.log(moveTen("codewars")) // should return "mynogkbc"