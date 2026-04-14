class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x:x[1])

        minheap = []  #[end, passenger]
        curpass = 0

        for num, start, end in trips:
            while minheap and minheap[0][0] <= start:
                curpass -= heapq.heappop(minheap)[1]

            curpass+=num
            if curpass > capacity:
                return False

            heapq.heappush(minheap, [end, num])
        
        return True

        