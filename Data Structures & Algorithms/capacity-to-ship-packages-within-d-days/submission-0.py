class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canship(cap):
            ships = 1 
            curcap = 0
            for w in weights:
                if curcap + w > cap:
                    ships+=1
                    if ships > days:
                        return False
                    curcap = 0
                curcap+=w
            return True
        
        while l <= r:
            mid = (l+r)//2
            if canship(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res