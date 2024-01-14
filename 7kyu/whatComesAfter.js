/*
You will be given two inputs: a string of words and a letter. For each string, return the alphabetic character after every instance of letter(case insensitive).
If there is a number, punctuation or underscore following the letter, it should not be returned.
*/

function comes_after(str, l) {
    let result = "";
    l = l.toLowerCase();

    for (let i = 1; i < str.length; i++) { // go over each el in the str starting from the second letter in the string
        console.log(str[i])
        if (str[i - 1].toLowerCase() === l && /[a-zA-Z]/.test(str[i])) {
            result += str[i];
        }
    }
    return result;
}

console.log(comes_after("Pirates say arrr", 'r')) // should return 'arr'