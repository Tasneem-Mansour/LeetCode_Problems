class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ####Solution 1 (doesnt work)#### time limit exceed
        # hashMap = {}           
        # res = []
        # for i in range(len(strs)):
        #     word = "".join(sorted(strs[i]))
        #     if word in hashMap:
        #         hashMap[word].append(strs[i])
        #     else:
        #         hashMap[word] = [strs[i]]
        #     print (hashMap)
        # for key, value in hashMap.items():
        #     res.append(value)
        
        # return res
                    
        ####Solution 2 ####    
        # "aet": ["eat", "tea", "ate"],
        # "ant": ["tan", "nat"],
        # "abt": ["bat"]

        hashMap = defaultdict(list)
        for i in range(len(strs)):
            sortedWord = "".join(sorted(strs[i]))

            hashMap[sortedWord].append(strs[i])

        return hashMap.values()










