class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ####Solution 1 (doesnt work)#### time limit exceeded in some TCs
        # hashMap = {}           
        # for i in range(len(strs)):
        #     word = "".join(sorted(strs[i]))
        #     if word in hashMap:
        #         hashMap[word].append(strs[i])
        #     else:
        #         hashMap[word] = [strs[i]]
        #     print (hashMap)
        # return hashMap.values()
                    
        ####Solution 2 ####    O(m*nlogn)
        # "aet": ["eat", "tea", "ate"],
        # "ant": ["tan", "nat"],
        # "abt": ["bat"]

        hashMap = defaultdict(list)
        for i in range(len(strs)):
            sortedWord = "".join(sorted(strs[i]))
            hashMap[sortedWord].append(strs[i])
        print(hashMap)
        return hashMap.values()

        ####Solution 3####       O(m*n)
        # hashMap = defaultdict(list)
        # for word in strs:
        #     count = [0] * 26    #a -> z
        #     for letter in word:
        #         count[ord(letter) - ord("a")] += 1
        #     hashMap[tuple(count)].append(word)

        # print(hashMap)
        # return hashMap.values()
            
        











