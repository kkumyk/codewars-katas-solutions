/*
You are going to be given a word. Your job will be to make sure that each character in that word has the exact same number of occurrences. You will return true if it is valid, or false if it is not.
For this kata, capitals are considered the same as lowercase letters. Therefore: "A" == "a"
The input is a string (with no spaces) containing [a-z],[A-Z],[0-9] and common symbols. The length will be 0 < length < 100.
*/

function validateWord(s) {

    let counter = {};

    [... new Set(s)].forEach(element => {
        if (!counter.hasOwnProperty(element)) {
            counter[element.toLowerCase()] = 0
        }
    });

    s.split("").forEach(el => (counter.hasOwnProperty(el.toLowerCase()) ? counter[el.toLowerCase()] += 1 : 0))

    return ([... new Set(Object.values(counter))].length > 1) ? false : true;
}

console.log(validateWord("bAc!abcddddc5!")); // should return false;