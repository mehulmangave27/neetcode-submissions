class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        arr = [1,2]

        sum = 0
        for i in range (2,n):
            sum = arr[i-2] + arr[i-1]
            arr.append(sum)

        return sum  
