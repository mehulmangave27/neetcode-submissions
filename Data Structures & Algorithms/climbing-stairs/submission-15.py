class Solution:
    def climbStairs(self, n: int) -> int:
        #[1,2,3,5,8]
        if n <= 2:
            return n
        res = [1,2]

        for i in range(n-3, -1, -1):
            res.append(res[-1]+res[-2])

        return res[-1]

        