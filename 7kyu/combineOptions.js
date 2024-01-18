/*
Write a function that takes two or more objects and returns a new object which combines all the input objects.
Objects are combined together so that the values of matching keys are added together.
*/

function combine(...args) {

    let objArr = [].concat(...args);
    let result = {};

    objArr.forEach(object => {
        for (key in object) {
            
            if (result[key]) { result[key] = result[key] + object[key] }
            else { result[key] = object[key] }
        }
    })
    return result;
}


combine({ a: 10, b: 20, c: 30 }, { a: 3, c: 6, d: 3 }) // Returns { a: 13, b: 20, c: 36, d: 3 }