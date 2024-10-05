class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ####Solution 1####
        # countNums = {}
        # heap = []
        # answer =[]
        # #count
        # for i in range(len(nums)):
        #     countNums[nums[i]] = 1 + countNums.get(nums[i], 0)  #add 1 to its value

        # #arrange by value 
        # for key in countNums:
        #     heapq.heappush(heap, (-countNums[key], key))

        # for i in range(k):
        #     answer.append(heapq.heappop(heap)[1])        #return [1] not [0] and not all of them
        
        # return answer

        ####Solution 2 - almost Bucket Sorting ####
        hashMap = {}
        freq = [[] for i in range(len(nums) +1)]
        res = []
        #count
        for i in range(len(nums)):
            hashMap[nums[i]] = 1 + hashMap.get(nums[i], 0)

        for n, c in hashMap.items():
            freq[c].append(n)      # k happened v times put it in index v 
        
        for i in range(len(freq)-1, 0, -1):
            # print(freq[i])
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

        



        