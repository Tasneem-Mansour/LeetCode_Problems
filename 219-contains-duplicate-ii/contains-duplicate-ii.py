class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # hashMap = {}
        # for i in range(len(nums)):
        #     hashMap[nums[i]] = 1 + hashMap.get(hashMap[nums[i]], 0)
        #     if hashMap[nums[i]] > 1 and nums[i] 
            

        
        # for key in hashMap:
        #     if hashMap[key] > 1 and nums[key]


        hset = {}
        for idx in range(len(nums)):
            if nums[idx] in hset and abs(idx - hset[nums[idx]]) <= k:
                return True
            hset[nums[idx]] = idx
        return False

        