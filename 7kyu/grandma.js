// replace "two", "too" and "to" with 2

function textin(s) {

    return s.split(" ").map(word => word.replace(/two|too|to/gi, "2")).join(" ");
}

console.log(textiin("Tomorrow send to her two text too."))