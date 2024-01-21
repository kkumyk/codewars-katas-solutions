const sumNested = arr => arr.flat(Infinity).reduce((a, b) => a + b, 0)

console.log(sumNested([1, [2, [3, [4]]]])) // 10