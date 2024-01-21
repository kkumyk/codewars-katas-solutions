/*
There are two lists, possibly of different lengths. The first one consists of keys, the second one consists of values.
Write a function createDict(keys, values) that returns a dictionary created from keys and values.
If there are not enough values, the rest of keys should have a None (JS null)value.
If there not enough keys, just ignore the rest of values.
*/

function createDict(keys, values) {

    let result = {};

    for (let i = 0; i < keys.length; i++) {
        result[keys[i]] = i < values.length ? values[i] : null;
    }

    return result;
};

console.log(createDict(['a', 'b', 'c', 'd'], [1, 2, 3])) // {'a': 1, 'b': 2, 'c': 3, 'd':null}
