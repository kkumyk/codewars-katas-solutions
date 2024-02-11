class Solution:
    def compress(self, chars: list[str]) -> int:
        
        res = []
        dic = {}

        if len(chars) == 1:
            res.append(chars[0])
        else:
            for char in chars:
                if char not in dic.keys():
                    dic[char] = 1
                else:
                    dic[char] += 1
        
        for k in dic.keys():
            if dic[k] == 1:
                res.append(k)
            elif dic[k] <= 10:
                res.append(k)
                res.append(str(dic[k]))
            else:
                res.append(k)
                res.extend(list(str(dic[k])))
        return len(res)




solution = Solution()
print(solution.compress(["a","a","b","b","c","c","c"]))  # ["a","2","b","2","c","3"]
