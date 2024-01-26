// A Tidy number is a number whose digits are in non-decreasing order.

function tidyNumber(n) {

    return parseInt(String(n).split("").map(s => Number(s)).sort((a, b) => a - b).join("")) === n;
}

console.log(tidyNumber(12)) // true