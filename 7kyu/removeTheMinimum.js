/*
Given an array of integers, remove the smallest value. Do not mutate the original array/list.
If there are multiple elements with the same value, remove the one with a lower index.
If you get an empty array/list, return an empty array/list.
*/

function removeSmallest(numbers) {
    /*
    Apply lets you invoke the function with arguments as an array.
    Apply uses Arrays and Always takes one or two Arguments.
    Inside a function, the value of this depends on how the function is called.
    Think about this as a hidden parameter of a function — just like the parameters declared in the function definition,
    this is a binding that the language creates for you when the function body is evaluated.
    In non–strict mode, this is always a reference to an object. In strict mode, it can be any value.
    */
    const min = Math.min.apply(this, numbers);

    return numbers.filter((num, idx, arr) => idx !== arr.indexOf(min));
}

console.log(removeSmallest([1, 2, 3, 4, 5])) // [2, 3, 4, 5]


