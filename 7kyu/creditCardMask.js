/*
Write a function maskify, which changes all but the last four characters into '#'.
*/

function maskify(cc) {
    
    return (cc.length < 4) ? cc : `${"#".repeat(cc.slice(0,cc.length-4).length)}` + cc.slice(-4);
}

console.log(maskify('4556364607935616')) // '############5616'
