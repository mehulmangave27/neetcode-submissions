class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #[1,4,6,2,2,1]
        #[Final, 1, 2, 2, 6, 4, 5] = min(4,5) = 4

        if len(cost) == 2:
            return min(cost[0], cost[1])

        res = [cost[-1], cost[-2]]

        for i in range(len(cost)-3, -1, -1):
            temp = cost[i] + min(res[-1], res[-2])
            res.append(temp)

        return min(res[-1], res[-2])