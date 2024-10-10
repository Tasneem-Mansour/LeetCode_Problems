class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ####Solution 1 #### not very efficient time comp = O(nlogn), space comp = O(n)
        # nums.sort()         #[0,1]
        # target = []         #[0,1,2]

        # for i in range(0, len(nums)+1):
        #     target.append(i)

        # while len(nums) != len(target):
        #     nums.append(0)

        # for i in range(len(nums)):
        #     if nums[i] != target[i]:
        #         return target[i]

        ####Solution 2 #### we can do better time comp = O(n), space comp = O(n)
        # n = len(nums)
        # missingNum = [0] * n+1          #[1,1,0,1]

        # for i in nums:
        #     missingNum[i] = 1

        # for i in range(len(missingNum)):
        #     if missingNum[i] == 0:
        #         return i
        # return 0
        
        ####Solution 3 #### time comp = O(n), space comp = O(1)
        n = len(nums)
        res = 0
        for i in range(0, n+1):
            res ^= i
        for num in nums:
            res ^= num

        return res