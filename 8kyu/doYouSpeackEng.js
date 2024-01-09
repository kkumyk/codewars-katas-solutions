/*
Given a string of arbitrary length with any ascii characters. Write a function to determine whether the string contains the whole word "English".
The order of characters is important -- a string "abcEnglishdef" is correct but "abcnEglishsef" is not correct.
Upper or lower case letter does not matter -- "eNglisH" is also correct.
Return value as boolean values, true for the string to contains "English", false for it does not.
*/

// Solution 1
function spEng(sentence) {
    return (sentence.match(/english/i)) ? true : false; // i - ignore case;
}

// Solution 2
function spEng(sentence) {
    return /english/i.test(sentence);
}

// Solution 3
function spEng(sentence) {
    return sentence.toLowercase().includes("english");
}