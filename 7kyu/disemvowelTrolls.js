// Write a function that takes a string and return a new string with all vowels removed.

function disemvowel(str) {

    return str.replace(/[aeoiu]/ig, "");
}


console.log(disemvowel("This website is for losers LOL!")) // "Ths wbst s fr lsrs LL!"