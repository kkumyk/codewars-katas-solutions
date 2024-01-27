/*
This time no story, no theory. The examples below show you how to write function accum:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
*/

function accum(str) {

    let arr = str.toLowerCase().split('')
    let newArr = [];

    for (let i = 0; i < arr.length; i++) {
        let subString = "";
        
        subString += arr[i].toUpperCase()
        subString+= arr[i].repeat(i+1).slice(0,-1); // delete last char in a string
        newArr.push(subString)
    }
    return newArr.join('-')
}

console.log(accum("mumbling"))
