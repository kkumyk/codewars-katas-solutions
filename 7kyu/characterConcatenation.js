/*
Given a string, you progressively need to concatenate the first letter from the left and the first letter to the right and "1",
then the second letter from the left and the second letter to the right and "2", and so on.
If the string's length is odd drop the central element.
*/

function charConcat(string) {

    let arr = string.split('');
    let result = [];

    for (let i = 1; i <= arr.length / 2; i++) {
        result.push(string[i - 1])
        result.push(string[string.length - i])
        result.push(i)
    }
    return result.join('');
}
console.log(charConcat("CodeWars")) // 'Cs1or2da3eW4'