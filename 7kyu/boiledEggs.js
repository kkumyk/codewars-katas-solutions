/*
- write a function, which takes a non-negative integer, representing the number of eggs to boil
- return the time in minutes (integer), which it takes to have all the eggs boiled
- you can put at most 8 eggs into the pot at once
- it takes 5 minutes to boil an egg
*/

function cookingTime(eggs) {

    let batches = Math.ceil(eggs/8)

    return batches * 5
}


console.log(cookingTime(20)) // 15