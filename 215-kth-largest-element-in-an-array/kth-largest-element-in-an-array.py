# from collections import heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        print(list(nums))

        #### Solution 1####
        # values = (heapq.nlargest(k, nums))
        # value = values.pop()
        # return value
        
        #### Solution 2####
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]

