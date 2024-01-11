/*
In a small town the population is p0 = 1000 at the beginning of a year.
The population regularly increases by 2% per year and moreover 50 new inhabitants per year come to live in the town.
How many years does the town need to see its population greater than or equal to p = 1200 inhabitants?
*/

function nbYear(p0, percent, aug, p, years = 0) {

    if (p0 < p) {
        return nbYear( p0 + parseInt(p0 * percent / 100) + aug, percent, aug, p, years + 1 );
    }
    return years
}

console.log(nbYear(1500, 5, 100, 5000)) //should return 15
