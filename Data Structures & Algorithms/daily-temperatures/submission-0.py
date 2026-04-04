class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = temperatures
        
        answer = []
        

        for i in range(0, len(temperatures)):
            for j in range(i, len(temperatures)):
                if res[j] > temperatures[i]:
                    answer.append(j-i)
                    break
                elif j == len(temperatures) - 1:
                    answer.append(0)

        return answer
            
            

            
                


          
                
                
        