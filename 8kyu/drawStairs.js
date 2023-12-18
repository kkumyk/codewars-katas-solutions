
/*
Given a number n, draw stairs using the letter "I", n tall and n wide, with the tallest in the top left.
*/

function drawStairs(n) {
  let result = [];
  
  for (let i = 0; i < n; i++) {
    result[i] = `${' '.repeat(i)}I`;
  }
  
  return result.join('\n');
}