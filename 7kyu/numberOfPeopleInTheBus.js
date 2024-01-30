/*
- input: an array of integer pairs
- each pair represent the number of people that get on and off the bus
- return the number of people who are still on the bus after the last bus 
*/

function busStop(arr) {

    let totalIn = 0;
    let totalOut = 0;

    arr.forEach(element => {
        totalIn += element[0];
        totalOut += element[1];
    });

    return totalIn - totalOut;
}


console.log(busStop([[3,0],[9,1],[4,10],[12,2],[6,1],[7,10]])) // 17