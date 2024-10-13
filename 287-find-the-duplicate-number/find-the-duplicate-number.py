class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #with modifying the array. time comp = O(n), space comp = O(1)
        # for i in range(len(nums)):
        #     index = abs(nums[i])
        #     if nums[index] < 0:
        #         return index
        #     nums[index] = -nums[index]

        #without modifying the array. time comp = O(n), space comp = O(1)
        slow = 0        
        fast = 0        

        while True:
            slow = nums[slow]           
            fast = nums[nums[fast]] 
            if slow == fast:
                break    
  
        slow2 = 0
        while slow != slow2:
            slow  = nums[slow]      
            slow2 = nums[slow2]     

        return slow