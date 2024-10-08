class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ####Solution 1####  O(n)
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] in hashMap and (i - hashMap[nums[i]]) <= k:
                return True
            hashMap[nums[i]] = i   
        return

        ####Solution 2 - sliding window####  O(n)

        window = set()   
        L = 0          

        for R in range(len(nums)):
            if R-L > k:   
                window.remove(nums[L])
                L += 1
            if nums[R] in window:
                return True
            window.add(nums[R])
        return

        