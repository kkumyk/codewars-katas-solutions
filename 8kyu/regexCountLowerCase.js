/*
Your task is simply to count the total number of lowercase letters in a string.
*/

// Solution 1
function lowercaseCount(str) {
    return (str.match(/[a-z]/g) || []).length;
}

// Solution 2
function lowercaseCount(str) {
    return str.replace(/[^a-z]/g,"").length;
}