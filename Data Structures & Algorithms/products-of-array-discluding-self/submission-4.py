class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0]*len(nums)
        suff = [0]*len(nums)
        pre[0] = suff[len(nums)-1] = 1 

        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
        
        for j in range(len(nums)-2, -1, -1):
            suff[j] = suff[j+1]*nums[j+1]

        res = []
        
        for i in range(len(nums)):
            res.append(pre[i]*suff[i])

        return res


