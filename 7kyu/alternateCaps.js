
function capitalize(s) {

    let even = [...s].map((l, i) => (i % 2 === 0 ? s[i].toUpperCase() : s[i]))
    let odd = [...s].map((l, i) => (i % 2 !== 0 ? s[i].toUpperCase() : s[i]))

    return [even.join(""), odd.join("")];
};

console.log(capitalize("abracadabra")) // ['AbRaCaDaBrA', 'aBrAcAdAbRa']