/*
Given an array of integers your solution should find the smallest integer.
For example:
Given [34, 15, 88, 2] your solution will return 2
Given [34, -345, -1, 100] your solution will return -345
You can assume, for the purpose of this kata, that the supplied array will not be empty.
*/

/*
In general, fn.apply(null, args) is equivalent to fn(...args) with the parameter spread syntax.
*/

// Solution 1
class SmallestIntegerFinder {
    findSmallestInt(args) {
        return Math.min.apply(null, args);
    }
}

// Solution 2
class SmallestIntegerFinder {
    findSmallestInt(args) {  // The rest parameter syntax allows us to represent an indefinite number of arguments
        return Math.min(...args)
    }
}
