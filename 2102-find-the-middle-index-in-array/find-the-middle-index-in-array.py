class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        if not nums:
            return

        totalSum = sum(nums)

        leftSum = 0
        index = 0
        for i in range(len(nums)):
            rightSum = totalSum - nums[i] - leftSum        

            if leftSum == rightSum:
                return i
            
            leftSum += nums[i]                             

        return -1
