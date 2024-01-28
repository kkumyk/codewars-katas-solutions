function scrollingText(str) {
    let result = [];

    for (let i = 0; i < str.length; i++) {
        result.push((str.slice(i) + str.slice(0, i)).toUpperCase());
    }
    return result;
}

console.log(scrollingText("milk"))