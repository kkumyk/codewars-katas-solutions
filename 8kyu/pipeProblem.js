/*
Given a list of unique numbers sorted in ascending order,
return a new list so that the values increment by 1 for each index from the minimum value
up to the maximum value (both included).

Example
Input:  1,3,5,6,7,8 Output: 1,2,3,4,5,6,7,8
*/


function pipeFix(numbers) {

    let result = [];

    let minValue = numbers[0];
    let maxValue = numbers.slice(-1)[0]


    for (let i = minValue; i <= maxValue; i++) {
        result.push(i)
    }

    return result;
}

console.log(pipeFix([6, 9])) // should return [6,7,8,9]