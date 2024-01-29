// fn to check if there are exactly four or six digits

function validatePin(pin) {

    return /^(\d{4}|\d{6})$/.test(pin)
}


console.log(validatePin("2382983")) // false