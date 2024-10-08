class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ####Solution1####  not very good approach   O(n^2)
        # for i in range(len(nums)):
        #     for j in range(1, len(nums)):
        #         if nums[i]   +nums[j] == target and i!=j:  
        #             return i, j


        ####Solution2####   good enough
        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in nums and i!= nums.index(complement) :
        #         return i, nums.index(complement) 



        ####Solution 3####
        # hashmap = {}                 #value -> index

        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i        

        # for i in range(len(nums)):
        #     complement = target - nums[i]
        #     if complement in hashmap and i != hashmap[complement]:
        #         return i, hashmap[complement] 

        ####Solution 4####  O(n)
        hashMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[nums[i]] = i
        return 
    


        