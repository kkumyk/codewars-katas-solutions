// Write a function that converts integer given as string into ASCII uppercase letters or spaces.

function convert(number) {

    let result = "";

    for (let i = 0; i < number.length; i++) {

        let num = number.slice(i, (i + 2))
        i += 1;
        result += String.fromCharCode(num);
    }
    return result;
}

console.log(convert("676584")) // "CAT