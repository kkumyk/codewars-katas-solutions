// Solution 1
function removeDuplicateWords(s) {
    let result = [];
    let wordsArray = s.split(" ");

    for (let i = 0; i < wordsArray.length; i++) {
        if (result.indexOf(wordsArray[i]) === -1) {
            result.push(wordsArray[i]);
        }
    }
    return result.join(" ");
}

// Solution 2
const removeDuplicateWords = s => [... new Set(s.split(" "))].join(" ");

console.log(removeDuplicateWords('alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'))

// 'alpha beta gamma delta'