/*
Imagine you start on the 5th floor of a building, then travel down to the 2nd floor, then back up to the 8th floor.
You have traveled a total of 3 + 6 = 9 floors of distance.
Given an array representing a series of floors you must reach by elevator,
return an integer representing the total distance travelled for visiting each floor in the array in order.
Array will always contain at least 2 floors.
*/

function elevatorDistance(array) {

    let distances = [];

    for (let i = 0; i < array.length - 1; i++) {
        distances.push(Math.abs(array[i] - array[i + 1]))
    }
    return distances.reduce((a, b) => a + b, 0);
}

console.log(elevatorDistance([5, 2, 8])) // 3 + 6 = 9