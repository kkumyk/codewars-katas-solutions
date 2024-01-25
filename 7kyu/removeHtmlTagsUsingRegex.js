
/*
. matches any one character.

+ sign matches one or more of the former items, which, as usual, we’ll assume is the previous character.
The list of possible matches is clear: the former character. And the number of matches is clear: one or more.

Difference between .+ and .+?

Both will match any sequence of one or more characters. The difference is that:

.+ is greedy and consumes as many characters as it can.
.+? is reluctant and consumes as few characters as it can.

*/

function removeTags(string) {

    return string.replace(/<.+?>/g, "")
}



console.log(removeTags("<img src='home.jpg'/>foto description")) // foto description