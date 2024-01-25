
// Write a regex to validate a 24 hours time string.

function validateTime(time) {

    let regex = /^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/;

    return regex.test(time);
}

console.log(validateTime('13:1')) // false

/*
/^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$/

() - match [0-1]?[0-9] OR 2[0-3] in ([0-1]?[0-9]|2[0-3])
? - The last character is optional as validateTime('1:00'), true
*/