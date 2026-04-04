class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        L, R = float('inf'), float('-inf')

        for _, start, end in trips:
            L = min(L, start)
            R = max(R, end)
        
        N = R - L + 1
        res = [0]*(N+1)

        for passengers, start, end in trips:
            res[start-L] += passengers
            res[end-L] -= passengers

        curpass = 0
        for cur in res:
            curpass += cur
            if curpass > capacity:
                return False
        return True