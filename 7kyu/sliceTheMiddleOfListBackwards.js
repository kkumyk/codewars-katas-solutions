/*
Write a function that takes a list of at least four elements as an argument and returns a list of the middle two or three elements in reverse order.
*/

// Solution 1
function reverseMiddle(array) {

    let listMiddle = Math.floor(array.length / 2) - 1; // 1
    return array.slice(listMiddle).reverse().slice(listMiddle);
}

console.log(reverseMiddle([1, 2, 3, 4, 5])) //  [ 4, 3, 2 ]

// Solution 2

const reverseMiddle2 = arr => {
    const midd = ~~(arr.length / 2) // 2; "~~" is a faster substitute for Math.floor() for positive numbers
    const start = midd - 1 // 1; to adjust 0 index

    const end = arr.length % 2 === 0 ? midd + 1 : midd + 2
  
    return arr.slice(start, end).reverse()
  }

  console.log(reverseMiddle2([1, 2, 3, 4, 5])) //  [ 4, 3, 2 ]