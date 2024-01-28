/*
- function that takes string as input and checks if it is a valid Russian postal code;
- a valid postcode:
    - 6 digits
    - cannot start with 0, 5, 7, 8, 9
    - no white spaces / letters / other symbols;
- empty string should also return false.
*/

function zipvalidate(postcode) {
    
    return /^[12346]\d{5}$/.test(postcode)
}

console.log(zipvalidate("02A483")) // false