
// Solution 1
// function toJadenCase(string) {

//     let result = "";
//     let words = string.split(" ");

//     for (let i = 0; i < words.length; i++) {
//         result += words[i].slice(0, 1).toUpperCase() + words[i].slice(1) + " ";
//     }
//     return result.trim();
// }


// Solution 2

function toJadenCase(string) {

    return string.split(" ").map(word => word.charAt(0).toUpperCase() + word.slice(1)).join(" ")
}


console.log(toJadenCase("How can mirrors be real if our eyes aren't real")) //"How Can Mirrors Be Real If Our Eyes Aren't Real"