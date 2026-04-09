from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        res = []

        for i in nums:
            count[i]+=1
        
        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)

        for i in range(k):
            a, b = heapq.heappop(heap)
            res.append(b)

        return res

            
        
            





        
        



        