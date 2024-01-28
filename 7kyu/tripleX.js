// return true if the first instance of "x" in the string is immediately followed by the string "xx"

function tripleX(str) {
    let idxOfX = str.indexOf("x");
    let threeChars = str.slice(idxOfX, idxOfX+3);
    console.log(threeChars)

    return threeChars === "xxx";
}

console.log(tripleX("abraxxxcadabra")) // true