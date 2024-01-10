/*
Given a string, turn each character into its ASCII character code and join them together - number total1:
'ABC' --> 'A' = 65, 'B' = 66, 'C' = 67 --> 656667
Then replace any incidence of the number 7 with the number 1, and call this number 'total2'
*/

function calc(x) {

  var total1 = [];
  var total2 = "";

  x.split('').forEach(function (letter) {
    total1 += letter.charCodeAt();
  })

  total1.split('').forEach(function (stringNumber) {
    (Number(stringNumber) === 7) ? total2 += 1 : total2 += Number(stringNumber);
  })

  var sum1 = total1.split("").reduce((a, b) => Number(a) + Number(b), 0);
  var sum2 = total2.split("").reduce((a, b) => Number(a) + Number(b), 0);

  return sum1 - sum2;
}

console.log(calc("abcdef"))