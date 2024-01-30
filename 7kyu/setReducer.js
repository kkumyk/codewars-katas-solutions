/*
- fn takes array of integers
- sequential numbers should return their count: 6,6,6,6 - 4
- numbers that don't repeat should return the count of 1
- repeat the above until the fn returns a single integer
*/

function setReducer(input) {
    if (input.length === 1) return input[0];

    let newInput = [];
    let count = 1;

    for (let i = 0; i < input.length; i++) {
        if (input[i] === input[i + 1]) {
            count += 1;
        } else {
            newInput.push(count);
            count = 1;
        }
    }

    console.log(newInput);
    
    return setReducer(newInput);
}

console.log(setReducer([9, 4, 1, 1, 1, 2, 3, 9, 4, 6, 2])) // 3