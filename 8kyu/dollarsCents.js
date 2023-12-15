/*
Dollars and Cents

The company you work for has just been awarded a contract to build a payment gateway.
In order to help move things along, you have volunteered to create a function that will take
a float and return the amount formatting in dollars and cents.

3 needs to become $3.00
3.1 needs to become $3.10

*/

function formatMoney(amount) {
    return `\$${amount.toFixed(2)}`
}

console.log(formatMoney(3.1))