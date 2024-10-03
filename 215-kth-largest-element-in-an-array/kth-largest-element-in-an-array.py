# from collections import heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        print(list(nums))
        # value = heapq.heappop(nums[k])
        values = (heapq.nlargest(k, nums))
        value = values.pop()


        return value
        