/*
Complete the function power_of_two/powerOfTwo (or equivalent, depending on your language) that determines if a given non-negative integer is a power of two.
*/

function isPowerOfTwo(n) {
    if (n <= 0) return false;
    if (n === 1) return true;

    while (n >= 3) {
        if (n % 2 !== 0) return false;
        n = parseInt(n / 2);
    }
    return n % 2 === 0;
};

console.log(isPowerOfTwo(4096)) // true