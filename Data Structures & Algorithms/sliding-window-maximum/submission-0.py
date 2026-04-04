class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k - 1
        win = []
        res = []

        while r < len(nums):
            for i in range(l, r+1):
                win.append(nums[i])
            res.append(max(win))
            l+=1
            r+=1
            win = []
        return res

        