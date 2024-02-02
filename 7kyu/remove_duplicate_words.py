#     let result = [];
#     let wordsArray = s.split(" ");
#
#     for (let i = 0; i < wordsArray.length; i++) {
#         if (result.indexOf(wordsArray[i]) === -1) {
#             result.push(wordsArray[i]);
#         }
#     }
#     return result.join(" ");
# }
#
# // Solution 2
# const removeDuplicateWords = s => [... new Set(s.split(" "))].join(" ");


def remove_duplicate_words(s):
    result = []
    wordsArray = s.split(" ")

    for word in wordsArray:
        if word not in result:
            result.append(word)
    return " ".join(result)


print(
    remove_duplicate_words(
        "alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta"
    )
)

#'alpha beta gamma delta'
