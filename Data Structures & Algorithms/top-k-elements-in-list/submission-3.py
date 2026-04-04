from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []

        heap = [(-freq, num) for num, freq in count.items()]
        heapq.heapify(heap)

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res



        
        



        