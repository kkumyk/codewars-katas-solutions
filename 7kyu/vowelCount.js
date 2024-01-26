/*
- return the number (count) of vowels in the given string.
- a, e, i, o, u are vowels but not y.
- the input string will only consist of lower case letters and/or spaces.
*/

function getCount(str) {

    return str.replace(/[^aeuoi$]/g, "").length;
}

console.log(getCount("abracadabra")) // 5