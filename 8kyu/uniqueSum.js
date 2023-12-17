// def unique_sum_2(lst):
//     return sum(list(dict.fromkeys(lst))) if lst else None
// print("The unique sum of the numbers in a given list is: ", unique_sum_2([2, 3, 3, 3, 6, 666, 666]))

/*
Given a list of integers values, your job is to return the sum of the values;
however, if the same integer value appears multiple times in the list, you can only count it once in your sum.
*/

function uniqueSum(lst) {
    let result = 0;

    if (lst.length != 0) {
        new Set(lst).forEach(el => result += el)
        return result;
    } return null;
}

console.log(uniqueSum([1, 3, 8, 1, 8])) // should return 12