// Complete the function/method so that it returns the url with anything after the anchor (#) removed.

// Solution 1
function removeUrlAnchor(url) {
    return url.includes("#") ? url.slice(0, url.indexOf("#")) : url;
}

// Solution 2
function removeUrlAnchor(url) {
    return url.split('#')[0];
}

console.log(removeUrlAnchor('www.codewars.com#about')) // 'www.codewars.com'