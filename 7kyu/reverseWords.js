function reverseWords(str) {

    return str.split(" ").map(s => s.split("").reverse().join("")).join(" ")
}

console.log(reverseWords('quick brown fox')) // 'kciuq nworb xof'