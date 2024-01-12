/*
Write a function that returns true if the number is a "Very Even" number.
If a number is a single digit, then it is simply "Very Even" if it itself is even.
If it has 2 or more digits, it is "Very Even" if the sum of its digits is "Very Even".
*/

function isVeryEvenNumber(n) {
    if (n < 10) {
        if (n % 2 == 0)
            return true;
        return false;
    }
    // .map(Number) calls Number on each value in the array (casting it to a number) and returns the array of results.
    const sum = n.toString().split('').map(Number).reduce((a, n) => a + n, 0);

    return isVeryEvenNumber(sum);
}


console.log(isVeryEvenNumber(88)) // should return false