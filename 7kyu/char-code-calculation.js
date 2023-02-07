function calc(x){

  var total1 = "";
  var total2 = "";

  var letters = x.split('');
  letters.forEach(function(letter){
    total1 += letter.charCodeAt(0);
  })

  var total2Numbers = total1.split('');

  total2Numbers.forEach(function(stringNumber){
    if (Number(stringNumber) === 7 ) {
      total2 += 1;
    } else {
      total2 += Number(stringNumber);
    }
  })

  var sum1 = total1.split("").reduce( (a, b) => Number(a) + Number(b), 0);
  var sum2 = total2.split("").reduce( (a, b) => Number(a) + Number(b), 0);
  var difference = sum1 - sum2;
  
  return difference;
}
