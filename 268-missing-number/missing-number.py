class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sorting O(nlogn) then binary search O(logn) -> O(nlogn)

        nums.sort()         #[0,1]
        
        target = []         #[0,1,2]

        for i in range(0, len(nums)+1):
            target.append(i)

        while len(nums) != len(target):
            nums.append(0)

        for i in range(len(nums)):
            if nums[i] != target[i]:
                return target[i]