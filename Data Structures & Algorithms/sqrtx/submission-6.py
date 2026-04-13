class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, (x//2)+1
        res = 0

        if x == 0:
            return 0
        if x == 1:
            return 1


        while l <= r:
            m = (l+r)//2

            if m*m == x:
                return m
            
            elif m*m < x:
                l = m+1
                res = m
            
            else:
                r = m-1
        
        return res


        