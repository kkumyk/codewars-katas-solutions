/*
An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
*/

function isIsogram(str) {

    let uniques = [...new Set(str.toLowerCase())].join("");
    let testCase = (uniques.length < str.length) ? false : true;

    return testCase;
}

console.log(isIsogram("moOse")) // false