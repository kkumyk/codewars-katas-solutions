
function checkBucket(bucket) {
    return (bucket.includes("gold")) ? true : false;
}

console.log(checkBucket(['stone', 'stone', 'gold', 'stone', 'stone',])); // should return true