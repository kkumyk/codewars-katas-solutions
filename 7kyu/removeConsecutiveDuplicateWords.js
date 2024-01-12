// Your task is to remove all consecutive duplicate words from a string, leaving only first words entries. 

function removeConsecutiveDuplicates(string) {

    let result = string.split(" ")[0] + " ";

    let words = string.split(" ");

    for (let i = 1; i < words.length; i++) {

        if (words[i] !== words[i - 1]) {
            result += words[i] + " "
        }
    }

    return result.trim();
}

console.log(removeConsecutiveDuplicates("alpha beta beta")) // should return "alpha beta"