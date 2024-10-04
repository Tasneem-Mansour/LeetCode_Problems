# from collections import heap
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ####Solution 0####
        nums.sort()
        return nums[len(nums)-k]

        #### Solution 1####        
        # heapq.heapify(nums)                # O(n)
        # print(list(nums))     
        # values = (heapq.nlargest(k, nums))
        # value = values.pop()
        # return value
        
        #### Solution 2####                # O(n + k*log n)
        # heapq.heapify(nums)                # O(n)
        # print(list(nums))
        # while len(nums) > k:
        #     heapq.heappop(nums)         
        # return nums[0]

        #### Solution 3#### Quick select   # O(n) but worst case -> O(n^2), worth it tho
        # k = len(nums) - k
        # def quickSelect(left, right):
        #     if left == right:
        #         return nums[left]
            
        #     # pivot = nums[right]

        #     pivotIndex = random.randint(left, right)
        #     pivot = nums[pivotIndex]      
        #     nums[pivotIndex], nums[right] = nums[right], nums[pivotIndex]

        #     p = left
        #     for i in range(left, right):
        #         if nums[i] <= pivot:
        #             nums[p], nums[i] = nums[i], nums[p]
        #             p += 1

        #     nums[p], nums[right] = nums[right], nums[p]       
        #     if p > k:
        #         return quickSelect(left, p - 1)
        #     elif p < k:   
        #         return quickSelect(p + 1, right) 
        #     else: 
        #         return nums[k]
        # return quickSelect(0, len(nums)-1)





