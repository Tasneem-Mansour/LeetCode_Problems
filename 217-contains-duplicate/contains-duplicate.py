class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #####Solution1#####
        setOfNums = set()
        for n in nums:
            if n in setOfNums:
                return True
            else:
                setOfNums.add(n)
        return False

        #####Solution2#####
        # setOfNums = set(nums)

        # if len(nums)==len(setOfNums):
        #     return False
        # else:
        #     return True

        ####Solution 3####
        # hashMap = {}
        # for i in range(len(nums)):
        #     hashMap[nums[i]] = 1 + hashMap.get(nums[i],0)
        #     if hashMap[nums[i]] > 1:
        #         return True
        # return

        