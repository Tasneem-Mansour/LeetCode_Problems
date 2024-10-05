class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(x, y):
            dis = x**2 + y**2
            return dis

        minHeap= []
        for x, y in points: 
            minHeap.append([distance(x,y), x, y])  


        heapq.heapify(minHeap)
        print(minHeap)
        res = []
        for i in range(k):
            dis, x, y = heapq.heappop(minHeap)
            res.append([x,y])

        return res    

             

           

        