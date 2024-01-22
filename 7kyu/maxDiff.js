/*
Implement a function that returns the diff b/w the largest and the smallest value in a given list / array.
- lst contains integers, that means it may contain some negative numbers
- if lst is empty or contains a single element, return 0
- lst is not sorted
*/


function maxDiff(list) {
    return list.length ? Math.max(...list) - Math.min(...list) : 0;
};

console.log(maxDiff([1, 2, 3, -4])) // 3 - (-4) == 7