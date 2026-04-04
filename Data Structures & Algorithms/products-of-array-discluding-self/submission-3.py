class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prod = 1
        zero = 0
        for i in nums:
            if i!=0:
                prod = prod*i
            else:
                zero+=1
        
        if zero==1:
            for i in range(len(nums)):
                if nums[i]==0:
                    res[i]=prod
                else:
                    res[i]=0
            return res
        elif zero>1:
            return res
        else:
            for i in range(len(nums)):
                res[i] = prod//nums[i]
            return res
