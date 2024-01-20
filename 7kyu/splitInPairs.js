/*
The aim of this kata is to split a given string into different strings of equal size (note size of strings is passed to the method).
*/

var splitInParts = function (s, partLength) {

    let result = [];

    for (let i = 0; i < s.length; i += partLength) {
        result.push(s.slice(i, partLength + i))
    }

    return result.join(" ");
}

console.log(splitInParts("supercalifragilisticexpialidocious", 3)) // "sup erc ali fra gil ist ice xpi ali doc iou s"






var splitInParts = function (s, partLength) {
    let result = [];

    for (var i = 0; i < s.length; i += partLength) {
        result.push(s.slice(i, partLength + i));
    }
    return result.join(' ')
}