class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, n in enumerate(nums):
            if n > 0:
                break
            if n == nums[i-1] and i > 0:
                continue
            
            l, r = i+1, len(nums)-1

            while l<r:
                three = n + nums[l] + nums[r]

                if three == 0:
                    res.append([n, nums[l], nums[r]])
                    l+=1
                    while l < len(nums) and nums[l] == nums[l-1]:
                        l+=1

                elif three > 0:
                    r-=1
                
                elif three < 0:
                    l+=1

        return res 

        




         

        