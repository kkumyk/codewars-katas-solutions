
function drawStairs(n) {
  let result = [];
  
  for (let i = 0; i < n; i++) {
    result[i] = `${' '.repeat(i)}I`;
  }
  
  return result.join('\n');
}


// function drawStairs(n) {
//     var count = 0;
//     var result = '';
  
//     while(n > count) {
//       result += ' '.repeat(count) + 'I';
//       count++;
//       if(n > count) result += '\n';
//     }
//     return result;
// }
