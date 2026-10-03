class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return max(nums)

        res = [nums[-1], nums[-2], nums[-3]+nums[-1]]
        if len(nums) == 3:
            return max(res)
        for i in range(len(nums)-4, -1, -1):
            res.append(nums[i] + max(res[-2], res[-3]))

        return max(res)




