class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        closetoopen = {"}":"{", "]":"[", ")":"("}

        for c in s:
            if c in closetoopen:
                if stack and stack[-1] == closetoopen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return False if len(stack)>0 else True 
            

            

        