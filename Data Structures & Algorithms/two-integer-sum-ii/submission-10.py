class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        add = 0

        while l<=r:
            add = numbers[l]+numbers[r]
            if add == target:
                return [l+1, r+1]

            elif target > add:
                l+=1
            else:
                r-=1

        


        
                
                    
        