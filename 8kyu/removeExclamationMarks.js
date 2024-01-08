/*
Remove all exclamation marks from the end of sentence.
*/

function remove(string) {
    return string.replace(/!+$/g,"");
}

console.log(remove("Hi!!!"))