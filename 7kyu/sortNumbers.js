/*
Finish the solution so that it sorts the passed in array of numbers.
If the function passes in an empty array or null/nil value then it should return an empty array.
*/

function solution(nums) {
    if (nums === null || nums === undefined || nums.length < 1) {
        return [];
    } return nums.sort((a, b) => a - b);
}

console.log(solution([1, 2, 3, 10, 5])) // should return [1,2,3,5,10]