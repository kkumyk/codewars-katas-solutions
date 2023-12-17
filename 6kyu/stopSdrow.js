/*
Write a function that takes in a string, and returns the same string,
but with all five or more letter words reversed.
Strings passed in will consist of only letters and spaces.
*/

function spinWords(string) {
    let result = [];

    for (let str of string.split(" ")) {
        if (str.length >= 5) {
            result.push(str.slice().split("").reverse().join(""))
        } else {
            result.push(str)
        }
    }
    return result.join(" ").trim();
}

console.log(spinWords("Hey fellow warriors")) // should return "Hey wollef sroirraw"