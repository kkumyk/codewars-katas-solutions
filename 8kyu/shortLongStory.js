/*
Given 2 strings, a and b, return a string of the form short+long+short,
with the shorter string on the outside and the longer string on the inside.
The strings will not be the same length, but they may be empty ( zero length ).
*/

function solution(a, b) {

    return (a.length > b.length) ? b + a + b : a + b + a;
}


console.log(solution('Soon', 'Me')) // should return 'MeSoonMe'