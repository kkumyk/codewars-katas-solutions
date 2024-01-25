/*
You are given a string phrase containing some potentially offensive words such as "bad," "mean," "ugly," "horrible," and "hideous."
Timmy wants to replace these words with the word "awesome" to make the message more positive. Your task is to implement a function,
that replaces all occurrences of these offensive words with "awesome" in the input string phrase.
*/

function filterWords(phrase) {

    let replacedWord = phrase.replace(/(bad|mean|ugly|horrible|hideous)/ig, 'awesome');

    return replacedWord.charAt(0).toUpperCase() + replacedWord.slice(1);
}

console.log(filterWords("You're Bad! timmy!")) // You're awesome! timmy!"