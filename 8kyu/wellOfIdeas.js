/*
Well of Ideas - Easy Version

For every good kata idea there seem to be quite a few bad ones!
In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'.
If there are one or two good ideas, return 'Publish!'.
If there are more than 2 return 'I smell a series!'.
If there are no good ideas, as is often the case, return 'Fail!'.
*/

function well(x) {

    if (x.slice().filter(x => (x === "good")).length > 2) {
        return 'I smell a series!'

    } else if (x.slice().filter(x => (x === "good")).length >= 1) {
        return "Publish!"
    } else {
        return "Fail!"
    }
}

console.log(well(["bad", "bad", "good", "bad", "bad", "bad", "bad", "bad"]))