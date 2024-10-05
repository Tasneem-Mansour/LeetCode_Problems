class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        countNums = {}
        heap = []
        answer =[]
        #count
        for i in range(len(nums)):
            countNums[nums[i]] = 1 + countNums.get(nums[i], 0)  #add 1 to its value

        #arrange by value 
        for key in countNums:
            heapq.heappush(heap, (-countNums[key], key))

        for i in range(k):
            answer.append(heapq.heappop(heap)[1])        #return [1] not [0] and not all of them
        
        return answer

        