/*
Your task is to return a number from a string.
*/

let filterString = function (value) {
    
    return Number(value.replace(/[^0-9]/g,""));

}

console.log(filterString("aa1bb2cc3dd")) // 123