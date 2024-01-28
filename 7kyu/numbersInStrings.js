// return largest number in a given string

function solve(s) {
    return parseInt(s.replace(/[a-z]/g, " ").split(" ").sort((a, b) => Number(b) - Number(a))[0])
}

console.log(solve("hf23lkjl1234")) // 1234