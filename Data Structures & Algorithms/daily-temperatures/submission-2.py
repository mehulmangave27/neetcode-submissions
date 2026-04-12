class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = [] #temp, ind

        for i, n in enumerate(temperatures):
            while stack and n > stack[-1][0]:
                stackt, stackind = stack.pop()
                res[stackind] = i - stackind
            stack.append([n,i])
        
        return res
