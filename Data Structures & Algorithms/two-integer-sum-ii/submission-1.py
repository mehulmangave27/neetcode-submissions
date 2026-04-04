class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0, len(numbers)-1
        temp = []

        for i in range(0,len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i]+numbers[j]==target:
                    temp.append(i+1)
                    temp.append(j+1)
                    return temp
                
                    
        